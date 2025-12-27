import pandas as pd
from dbfread import DBF
import os

CSV_PATH = "AI-Empowered-Software-Development-For-Educators/02-Lectures-And-Practices/module5/data/china_tourism.csv"
DBF_PATH = "AI-Empowered-Software-Development-For-Educators/02-Lectures-And-Practices/module5/data/青藏高原核心旅游资源.dbf"

print("Loading existing CSV...")
df_csv = pd.read_csv(CSV_PATH)
print(f"CSV Rows: {len(df_csv)}")

print("Loading DBF...")
table = DBF(DBF_PATH, encoding='utf-8') # 或 gbk，刚才看是utf-8成功的
df_dbf = pd.DataFrame(iter(table))
print(f"DBF Rows: {len(df_dbf)}")

# --- 数据转换 ---
# 目标列: City, Name, Rating, Sold_Price, Price_Source, Level, Address, Intro, Level_Official, Lat_Official, Lng_Official, Rating_Clean

new_rows = []

for _, row in df_dbf.iterrows():
    # 1. City (去 "市")
    city = str(row['市']).replace('市', '').strip()
    if not city or city == 'nan':
        # 如果市为空，尝试用区/州
        city = str(row['区']).replace('市', '').strip()
        
    # 2. Level
    level = str(row['景区等']).strip() # 假设已经是 "4A" 格式
    if level not in ['5A', '4A', '3A', '2A', '1A']:
        level = '' # 丢弃不规范的等级
        
    # 3. Price
    try:
        price = float(row['平均门'])
    except:
        price = 0.0
        
    new_row = {
        'City': city,
        '名字': row['景区名'],
        'Rating': 0.0, # DBF没评分，设为0
        'Sold_Price': price,
        'Price_Source': '[DBF来源]',
        'Level': level,
        'Address': f"{row['省']}{row['市']}{row['区']}",
        'Intro': f"主类:{row['景区主']}, 细类:{row['景区细']}",
        'Level_Official': level, # 假设DBF也是官方数据
        'Lat_Official': row['修正纬'],
        'Lng_Official': row['修正经'],
        'Rating_Clean': 0.0
    }
    new_rows.append(new_row)

df_new = pd.DataFrame(new_rows)

# --- 合并 ---
print("Merging...")
# 确保列名一致 (只取 CSV 中存在的列)
common_cols = df_csv.columns.tolist()
# 补齐 df_new 中缺失的列（如果有）
for col in common_cols:
    if col not in df_new.columns:
        df_new[col] = None

df_new = df_new[common_cols]

# 追加
df_final = pd.concat([df_csv, df_new], ignore_index=True)

# 去重 (Name 相同保留后者 - 假设 DBF 数据质量更高)
# 修正: 必须按 [City, 名字] 联合去重，防止不同城市的同名景点被误删！
df_final.drop_duplicates(subset=['City', '名字'], keep='last', inplace=True)

print(f"Final Rows: {len(df_final)}")

# 保存
df_final.to_csv(CSV_PATH, index=False, encoding='utf-8-sig')
print("Done! Qinghai data added.")
