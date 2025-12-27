from dbfread import DBF
import pandas as pd

DBF_PATH = "AI-Empowered-Software-Development-For-Educators/02-Lectures-And-Practices/module5/data/青藏高原核心旅游资源.dbf"

try:
    table = DBF(DBF_PATH, encoding='utf-8') # 尝试 utf-8
    df = pd.DataFrame(iter(table))
    print("Columns:", df.columns.tolist())
    print(df.head())
except Exception as e:
    print(f"Error: {e}")
    # 如果 utf-8 失败，通常是 gbk
    print("Retrying with GBK...")
    try:
        table = DBF(DBF_PATH, encoding='gbk')
        df = pd.DataFrame(iter(table))
        print("Columns:", df.columns.tolist())
        print(df.head())
    except Exception as e2:
        print(f"Fatal Error: {e2}")
