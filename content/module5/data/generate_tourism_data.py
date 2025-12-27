import pandas as pd
import glob
import os
import ast
import re
import numpy as np

# --- 配置 ---
DATA_DIR = "AI-Empowered-Software-Development-For-Educators/02-Lectures-And-Practices/module5/data/citydata"
OUTPUT_FILE = "AI-Empowered-Software-Development-For-Educators/02-Lectures-And-Practices/module5/data/china_tourism_raw.csv"

def extract_price_info(ticket_str):
    """
    解析门票字符串，返回 (sold_price, price_source_str)
    """
    if pd.isna(ticket_str) or ticket_str == '':
        return 0, ""
    
    # 1. 处理 "免费" 或纯数字
    if "免费" in str(ticket_str):
        return 0, "[免费:0]"
    
    try:
        # 尝试解析字典字符串 "{'项目': ['¥90']}"
        if isinstance(ticket_str, str) and ticket_str.strip().startswith("{"):
            ticket_dict = ast.literal_eval(ticket_str)
        else:
            # 可能是纯文本，尝试直接提取数字
             # 简单的正则提取，作为一个备选方案
            prices = re.findall(r'(\d+\.?\d*)', str(ticket_str))
            if prices:
                 # 这种情况下很难区分项目，就统一标记为"未知项目"
                 return float(prices[0]), f"[未知项目:{prices[0]}]"
            return 0, ""

    except (ValueError, SyntaxError):
        return 0, "" # 解析失败，视为无价格

    if not isinstance(ticket_dict, dict) or not ticket_dict:
        return 0, ""

    # 2. 提取价格并应用策略
    extracted_items = [] # 存储 (项目名, 价格数值)
    
    for name, price_list in ticket_dict.items():
        if not price_list: continue
        price_str = price_list[0] # 取第一个价格字符串 '¥90起'
        
        # 提取数字
        nums = re.findall(r'(\d+\.?\d*)', str(price_str))
        if nums:
            val = float(nums[0])
            clean_name = name.replace('\n', '').strip()
            extracted_items.append((clean_name, val))

    if not extracted_items:
        return 0, ""

    # 3. 生成 Price_Source 字符串
    # 格式: [成人票:90],[学生票:45]
    source_parts = [f"[{item[0]}:{item[1]}]" for item in extracted_items]
    price_source_str = ",".join(source_parts)

    # 4. 计算 Sold_Price (智能策略)
    # 优先级关键词
    high_priority_keywords = ["成人", "门票", "通票"]
    low_priority_keywords = ["儿童", "老人", "学生", "优待", "车", "导游", "柜"]
    
    candidates = []
    
    for name, price in extracted_items:
        # 排除低优先级 (比如仅是一个车票)
        is_low = any(k in name for k in low_priority_keywords)
        # 必须是高优先级
        is_high = any(k in name for k in high_priority_keywords)
        
        if is_high and not is_low:
             candidates.append(price)
    
    final_price = 0
    if candidates:
        # 如果有明确的"成人门票"，取其中的最小值 (通常是基础门票)
        final_price = min(candidates) 
    else:
        # 如果没有明确标识，取所有提取出的价格的中位数
        all_prices = [p for n, p in extracted_items]
        if all_prices:
            final_price = np.median(all_prices)
            
    return final_price, price_source_str

def extract_level(intro_str):
    """从介绍中提取 5A/4A 景区等级"""
    if pd.isna(intro_str): return ""
    match = re.search(r'([1-5]A)级?景区', str(intro_str))
    if match:
        return match.group(1)
    return ""

def process_files():
    all_data = []
    files = glob.glob(os.path.join(DATA_DIR, "*.csv"))
    
    print(f"Found {len(files)} CSV files in {DATA_DIR}")
    
    for f in files:
        try:
            # 从文件名提取城市
            city_name = os.path.basename(f).replace('.csv', '')
            
            # 读取CSV，忽略错误行
            df = pd.read_csv(f, on_bad_lines='skip')
            
            # 必须包含的列
            if '名字' not in df.columns: continue
            
            # 逐行处理
            for index, row in df.iterrows():
                # 复制原始行数据
                row_data = row.to_dict()
                
                # 计算新字段
                price, source = extract_price_info(row.get('门票', ''))
                level = extract_level(row.get('介绍', ''))
                
                # 评分处理 (尝试转换为float，保留原始值在 '评分' 列，新增一个清洗后的 'Rating_Clean')
                raw_rating = row.get('评分', 0)
                try:
                    rating_clean = float(raw_rating)
                except:
                    rating_clean = 0.0
                
                # 添加新字段
                row_data['City'] = city_name
                row_data['Sold_Price'] = price
                row_data['Price_Source'] = source
                row_data['Level_Raw'] = level
                row_data['Rating_Clean'] = rating_clean

                all_data.append(row_data)
                
        except Exception as e:
            print(f"Error processing {f}: {e}")

    # 合并
    final_df = pd.DataFrame(all_data)
    
    # 调整列顺序: City 放在第一列
    cols = ['City'] + [c for c in final_df.columns if c != 'City']
    final_df = final_df[cols]
    
    # 保存
    final_df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8-sig')
    
    # 统计
    print("-" * 30)
    print(f"Processing Complete!")
    print(f"Total Rows: {len(final_df)}")
    print(f"Rows with Price > 0: {len(final_df[final_df['Sold_Price'] > 0])}")
    print(f"Rows with 5A Level: {len(final_df[final_df['Level_Raw'] == '5A'])}")
    print(f"Saved to: {OUTPUT_FILE}")
    print("-" * 30)

if __name__ == "__main__":
    process_files()