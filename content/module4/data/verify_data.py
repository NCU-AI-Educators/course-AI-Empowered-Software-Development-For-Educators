import pandas as pd
import os

# 获取脚本所在目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(filename):
    return os.path.join(SCRIPT_DIR, filename)

def verify_hok():
    print("--- Verifying Honor of Kings Data ---")
    df = pd.read_excel(get_path('honor_of_kings.xlsx'))
    print(f"Total Rows: {len(df)}")
    print("Top 3 Mages (Win Rate):")
    print(df[df['职业'] == '法师'].sort_values('胜率', ascending=False)[['英雄', '胜率']].head(3))

def verify_survey():
    print("\n--- Verifying Survey Data ---")
    df = pd.read_excel(get_path('survey.xlsx'))
    print(f"Total Rows: {len(df)}")
    print("Head (first 5 rows):")
    print(df.head())

def verify_grades():
    print("\n--- Verifying Grades Data ---")
    df = pd.read_excel(get_path('final_grades.xlsx'))
    print(f"Total Rows: {len(df)}")
    print("Head (first 5 rows):")
    print(df.head())

if __name__ == "__main__":
    verify_hok()
    verify_survey()
    verify_grades()
