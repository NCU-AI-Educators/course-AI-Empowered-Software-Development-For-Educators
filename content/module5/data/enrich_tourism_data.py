import pandas as pd
import os

# --- 配置 ---
RAW_DATA_FILE = "AI-Empowered-Software-Development-For-Educators/02-Lectures-And-Practices/module5/data/china_tourism_raw.csv"
OFFICIAL_DATA_FILE = "AI-Empowered-Software-Development-For-Educators/02-Lectures-And-Practices/module5/data/A级景区分省.xlsx"
OUTPUT_FILE = "AI-Empowered-Software-Development-For-Educators/02-Lectures-And-Practices/module5/data/china_tourism_final.csv"

def normalize_name(name):
    """标准化景点名称，去除常见干扰词，提高匹配率"""
    if pd.isna(name): return ""
    name = str(name).strip()
    # 去除括号及内容 (如 "三亚(天涯海角)")
    import re
    name = re.sub(r'\(.*?\)', '', name)
    name = re.sub(r'（.*?）', '', name)
    return name

def enrich_data():
    print("Loading raw data...")
    df_raw = pd.read_csv(RAW_DATA_FILE)
    print(f"Raw data rows: {len(df_raw)}")

    print("Loading official A-level dataset...")
    # 读取 '总表' sheet
    df_official = pd.read_excel(OFFICIAL_DATA_FILE, sheet_name='总表')
    print(f"Official data rows: {len(df_official)}")
    
    # --- 1. 准备匹配键 ---
    # 我们创建一列 normalized_name 用于匹配
    df_raw['match_key'] = df_raw['名字'].apply(normalize_name)
    df_official['match_key'] = df_official['景区名称'].apply(normalize_name)
    
    # 字典结构: match_key -> (Level, Lat, Lng)
    # 如果有重名，后面的覆盖前面的 (通常没事)
    official_dict = {}
    for _, row in df_official.iterrows():
        key = row['match_key']
        if key:
            official_dict[key] = {
                'Level': row['景区等级'],
                'Lat': row['纬度BD'],
                'Lng': row['经度BD']
            }
            
    # --- 数据补丁 (Manual Patches) ---
    # 修正已知的数据源错误
    patches = {
        "燕山趣园景区": "1A",
        "修武县伊赛牛肉工业旅游": "1A",
        "和政县罗家集乡三岔沟景区": "2A"
    }
    
    for name, correct_level in patches.items():
        norm_name = normalize_name(name)
        if norm_name in official_dict:
            official_dict[norm_name]['Level'] = correct_level
            print(f"Patched: {name} -> {correct_level}")
            
    # 移除已取消评级的景区
    removals = ["五指山热带雨林风景区"] # 原始数据中可能有换行符，normalize后会去掉
    for name in removals:
        norm_name = normalize_name(name)
        # 注意：原始数据里可能是 "五指山热带雨林风景区(水\n满区)"，normalize后变成 "五指山热带雨林风景区"
        if norm_name in official_dict:
            del official_dict[norm_name]
            print(f"Removed: {name}")

    # 准备模糊匹配列表：按长度降序排列，优先匹配长词（更准）
    sorted_official_keys = sorted(official_dict.keys(), key=lambda x: len(str(x)), reverse=True)
    # 过滤掉太短的词 (比如2个字以下的)，防止误判
    sorted_official_keys = [k for k in sorted_official_keys if len(str(k)) > 2]

    print("Enriching data with Fuzzy Match (this might take a while)...")
    
    # --- 3. 填充数据 ---
    levels = []
    lats = []
    lngs = []
    
    match_count = 0
    exact_match_count = 0
    fuzzy_match_count = 0
    
    total_rows = len(df_raw)
    
    for index, row in df_raw.iterrows():
        if index % 1000 == 0:
            print(f"Processing row {index}/{total_rows}...")
            
        key = row['match_key']
        info = None
        
        # 策略 1: 精确匹配
        info = official_dict.get(key)
        if info:
            exact_match_count += 1
        
        # 策略 2: 模糊匹配 (如果没有精确匹配)
        if not info and len(str(key)) > 1:
            # 遍历官方名称列表
            for off_key in sorted_official_keys:
                # 情况 A: CSV名字 包含 官方名字 (e.g. "北京故宫博物院" 包含 "故宫博物院")
                if off_key in str(key):
                    info = official_dict[off_key]
                    fuzzy_match_count += 1
                    break
                
                # 情况 B: 官方名字 包含 CSV名字 (e.g. "黄山风景名胜区" 包含 "黄山")
                # 只有当 CSV 名字足够长时才允许这种情况，防止匹配到 "公园"
                if len(str(key)) > 2 and str(key) in off_key:
                    info = official_dict[off_key]
                    fuzzy_match_count += 1
                    break
        
        if info:
            match_count += 1
            levels.append(info['Level'])
            lats.append(info['Lat'])
            lngs.append(info['Lng'])
        else:
            levels.append(None)
            lats.append(None)
            lngs.append(None)
            
    df_raw['Level_Official'] = levels
    df_raw['Lat_Official'] = lats
    df_raw['Lng_Official'] = lngs
    
    # --- 4. 最终字段整合 ---
    # Level: 优先用官方，否则用 Raw
    df_raw['Level'] = df_raw['Level_Official'].fillna(df_raw['Level_Raw'])
    
    # [Final Clean] 强制清洗 Level 列，只保留合法的 1A-5A
    valid_levels = ['5A', '4A', '3A', '2A', '1A']
    df_raw.loc[~df_raw['Level'].isin(valid_levels), 'Level'] = None
    
    # 删除临时列
    df_raw.drop(columns=['match_key'], inplace=True)
    
    # --- 5. 保存 ---
    df_raw.to_csv(OUTPUT_FILE, index=False, encoding='utf-8-sig')
    
    # --- 统计 ---
    print("-" * 30)
    print("Enrichment Complete!")
    print(f"Total Matched: {match_count} ({match_count/len(df_raw):.1%})")
    print(f"  - Exact Matches: {exact_match_count}")
    print(f"  - Fuzzy Matches: {fuzzy_match_count}")
    print(f"Final 5A/4A Stats:")
    print(df_raw['Level'].value_counts().head(10))
    print(f"Saved to: {OUTPUT_FILE}")
    print("-" * 30)

if __name__ == "__main__":
    enrich_data()
