import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os


def generate_duration_boxplot(file_path):
    # 1. 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"错误: 找不到文件 '{file_path}'")
        return

    print("正在读取数据...")
    try:
        # 读取CSV文件
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"读取CSV文件失败: {e}")
        return

    # 2. 数据清洗
    print("正在清洗数据...")
    
    # 检查我们需要用到的列是否存在
    if 'title_year' not in df.columns or 'duration' not in df.columns:
        print("错误: CSV文件中缺少 'title_year' 或 'duration' 列")
        return

    # 统计清洗前的数据量
    original_count = len(df)

    # 删除 'title_year' 或 'duration' 为空 (NaN) 的行
    df_clean = df.dropna(subset=['title_year', 'duration']).copy()

    # 将年份转换为整数 (原始数据通常是浮点数，如 2009.0)
    df_clean['title_year'] = df_clean['title_year'].astype(int)

    # 过滤掉时长不合理的数据（例如：时长小于10分钟或大于300分钟的极端值，可选）
    # df_clean = df_clean[(df_clean['duration'] > 10) & (df_clean['duration'] < 300)]

    # 按年份排序，确保图表的时间轴是正确的
    df_clean = df_clean.sort_values('title_year')

    print(f"清洗完成。原始数据: {original_count} 行，清洗后: {len(df_clean)} 行。")

    # 3. 生成箱线图
    print("正在生成图表...")
    
    # 设置图表风格 (注意：必须在 set_theme 中通过 rc 参数设置字体，否则会被默认样式覆盖)
    sns.set_theme(style="whitegrid", rc={
        'font.sans-serif': ['SimHei', 'Arial Unicode MS', 'sans-serif'],
        'axes.unicode_minus': False
    })
    
    # 创建画布大小
    plt.figure(figsize=(20, 10))

    # 绘制箱线图
    # x轴: 年份, y轴: 时长
    boxplot = sns.boxplot(
        x='title_year', 
        y='duration', 
        data=df_clean, 
        palette="viridis",
        linewidth=1
    )

    # 4. 图表美化
    plt.title('电影时长分布统计 (按年份)', fontsize=20)
    plt.xlabel('年份', fontsize=14)
    plt.ylabel('时长 (分钟)', fontsize=14)
    
    # 旋转x轴的年份标签，防止重叠
    plt.xticks(rotation=90, fontsize=10)
    
    # 调整布局以防止标签被截断
    plt.tight_layout()

    # 5. 保存或显示
    output_file = 'movie_duration_boxplot.png'
    plt.savefig(output_file)
    print(f"图表已保存为: {output_file}")
    
    # 如果在支持GUI的环境下运行，可以取消下面这行的注释来直接显示
    # plt.show()

if __name__ == "__main__":
    # 假设csv文件在当前目录下
    csv_file = 'movie_metadata.csv'
    generate_duration_boxplot(csv_file)