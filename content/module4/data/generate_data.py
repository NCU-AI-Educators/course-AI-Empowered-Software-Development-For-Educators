import pandas as pd
import numpy as np
import random
import os

# 设置随机种子以保证结果可复现
np.random.seed(42)
random.seed(42)

# 获取脚本所在目录
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(filename):
    return os.path.join(SCRIPT_DIR, filename)

def generate_hok_data():
    """生成王者荣耀英雄数据 (Lessons 13-14)"""
    heroes = [
        # 射手 (Archer)
        ('鲁班七号', '射手'), ('后羿', '射手'), ('孙尚香', '射手'), ('马可波罗', '射手'), ('狄仁杰', '射手'),
        ('伽罗', '射手'), ('公孙离', '射手'), ('黄忠', '射手'), ('百里守约', '射手'), ('虞姬', '射手'),
        ('李元芳', '射手'), ('艾琳', '射手'), ('蒙犽', '射手'), ('成吉思汗', '射手'), ('戈娅', '射手'),
        ('莱西奥', '射手'),
        
        # 法师 (Mage)
        ('妲己', '法师'), ('安琪拉', '法师'), ('王昭君', '法师'), ('甄姬', '法师'), ('诸葛亮', '法师'),
        ('貂蝉', '法师'), ('上官婉儿', '法师'), ('不知火舞', '法师'), ('武则天', '法师'), ('弈星', '法师'),
        ('海月', '法师'), ('嬴政', '法师'), ('小乔', '法师'), ('周瑜', '法师'), ('张良', '法师'),
        ('墨子', '法师'), ('干将莫邪', '法师'), ('沈梦溪', '法师'), ('西施', '法师'), ('杨玉环', '法师'),
        ('女娲', '法师'), ('米莱狄', '法师'), ('扁鹊', '法师'), ('高渐离', '法师'), ('芈月', '法师'),
        ('司马懿', '法师'), ('嫦娥', '法师'), ('金蝉', '法师'),
        
        # 战士 (Warrior)
        ('亚瑟', '战士'), ('吕布', '战士'), ('铠', '战士'), ('花木兰', '战士'), ('李信', '战士'),
        ('狂铁', '战士'), ('老夫子', '战士'), ('达摩', '战士'), ('关羽', '战士'), ('马超', '战士'),
        ('曜', '战士'), ('蒙恬', '战士'), ('孙策', '战士'), ('杨戬', '战士'), ('哪吒', '战士'),
        ('雅典娜', '战士'), ('宫本武藏', '战士'), ('橘右京', '战士'), ('夏洛特', '战士'), ('赵怀真', '战士'),
        ('姬小满', '战士'), ('曹操', '战士'), ('典韦', '战士'),
        
        # 坦克 (Tank)
        ('程咬金', '坦克'), ('项羽', '坦克'), ('廉颇', '坦克'), ('白起', '坦克'), ('夏侯惇', '坦克'),
        ('猪八戒', '坦克'), ('刘邦', '坦克'), ('苏烈', '坦克'), ('刘禅', '坦克'), ('东皇太一', '坦克'),
        ('牛魔', '坦克'), ('张飞', '坦克'), ('阿古朵', '坦克'),
        
        # 刺客 (Assassin)
        ('李白', '刺客'), ('韩信', '刺客'), ('兰陵王', '刺客'), ('阿轲', '刺客'), ('孙悟空', '刺客'),
        ('镜', '刺客'), ('澜', '刺客'), ('娜可露露', '刺客'), ('赵云', '刺客'), ('百里玄策', '刺客'),
        ('元歌', '刺客'), ('司空震', '刺客'), ('云中君', '刺客'), ('裴擒虎', '刺客'), ('暃', '刺客'),
        
        # 辅助 (Support)
        ('蔡文姬', '辅助'), ('瑶', '辅助'), ('明世隐', '辅助'), ('孙膑', '辅助'), ('大乔', '辅助'),
        ('庄周', '辅助'), ('鬼谷子', '辅助'), ('盾山', '辅助'), ('鲁班大师', '辅助'), ('朵莉亚', '辅助'),
        ('桑启', '辅助'), ('太乙真人', '辅助'), ('钟馗', '辅助')
    ]
    
    # 扩展到100+数据 (通过添加编号或重复职业生成虚拟英雄)
    data = []
    for name, job in heroes:
        win_rate = round(random.uniform(0.45, 0.51), 3) # Lower max to 0.51 to avoid beating top 3
        ban_rate = round(random.uniform(0.0, 0.8), 3)
        # 给特定英雄设定高胜率以配合课程Demo
        if name == '武则天': win_rate = 0.541
        if name == '弈星': win_rate = 0.538
        if name == '海月': win_rate = 0.525
        if name == '鲁班七号': win_rate = 0.512
        
        data.append([name, job, win_rate, ban_rate])
        
    df = pd.DataFrame(data, columns=['英雄', '职业', '胜率', 'Ban率'])
    output_path = get_path('honor_of_kings.xlsx')
    df.to_excel(output_path, index=False)
    print(f"Generated {output_path} with {len(df)} rows.")

def generate_survey_data():
    """生成科研问卷脏数据 (Lesson 15)"""
    ids = range(1, 501)
    genders = np.random.choice(['男', '女'], 500, p=[0.4, 0.6])
    satisfaction = np.random.choice([1, 2, 3, 4, 5], 500, p=[0.05, 0.1, 0.2, 0.4, 0.25])
    
    df = pd.DataFrame({
        'ID': ids,
        '性别': genders,
        '满意度': satisfaction
    })
    
    # 制造脏数据
    # 1. 缺失值
    df.loc[random.sample(range(500), 20), '满意度'] = np.nan
    
    # 2. 异常值
    df.loc[random.sample(range(500), 2), '满意度'] = 100
    
    # 3. 重复值 (复制前5行并追加)
    duplicates = df.head(5).copy()
    df = pd.concat([df, duplicates], ignore_index=True)
    
    output_path = get_path('survey.xlsx')
    df.to_excel(output_path, index=False)
    print(f"Generated {output_path} with {len(df)} rows (including dirty data).")

def generate_grades_data():
    """生成学生成绩数据 (Lesson 16)"""
    # 生成随机中文名
    surnames = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜']
    names_char = ['伟', '芳', '娜', '敏', '静', '秀英', '丽', '强', '磊', '军', '洋', '勇', '艳', '杰', '娟', '志强', '玉兰', '建华', '文', '明', '超', '秀兰', '霞', '平', '刚', '桂英']
    
    names = []
    for _ in range(150):
        s = random.choice(surnames)
        n = random.choice(names_char)
        names.append(s + n)

    classes = np.random.choice([1, 2, 3], 150)
    midterm = np.random.randint(60, 100, 150)
    final = np.random.randint(50, 100, 150)
    
    df = pd.DataFrame({
        'ID': range(101, 251),
        'Name': names,
        'Class': classes,
        'Midterm': midterm,
        'Final': final
    })
    
    # 制造缺考数据 (Final为空)
    df.loc[random.sample(range(150), 2), 'Final'] = np.nan
    
    # 调整班级平均分以配合Demo (让2班最高)
    df.loc[df['Class'] == 2, 'Final'] += 5
    df.loc[df['Class'] == 2, 'Final'] = df.loc[df['Class'] == 2, 'Final'].clip(upper=100)
    
    # 制造不及格 (总评 < 60)
    # 简单粗暴地把几个人的期末分改低
    df.loc[0:5, 'Final'] = 30
    df.loc[0:5, 'Midterm'] = 40
    
    output_path = get_path('final_grades.xlsx')
    df.to_excel(output_path, index=False)
    print(f"Generated {output_path} with {len(df)} rows.")

def generate_movies_data():
    """生成电影市场数据 (Lessons 15-16) - 使用真实IMDB数据"""
    raw_path = get_path('movie_metadata.csv')
    if not os.path.exists(raw_path):
        print(f"Error: {raw_path} not found. Please download it first.")
        return

    # 读取真实数据
    df_raw = pd.read_csv(raw_path)
    
    # 提取所需列并重命名
    # movie_title, genres, budget, gross, imdb_score, director_name, title_year
    df = df_raw[['movie_title', 'genres', 'budget', 'gross', 'imdb_score', 'director_name', 'title_year']].copy()
    df.columns = ['Title', 'Genre', 'Cost', 'Revenue', 'Rating', 'Director', 'Year']
    
    # 数据清洗与转换
    # 1. Title: 去除末尾的特殊字符 (原数据中有 \xa0)
    df['Title'] = df['Title'].str.strip()
    
    # 2. Genre: 原数据是 "Action|Adventure", 我们只取第一个作为主类型
    # 2. Genre: 原数据是 "Action|Adventure", 我们只取第一个作为主类型，并翻译为中文
    genre_map = {
        'Action': '动作', 'Adventure': '冒险', 'Drama': '剧情', 'Animation': '动画',
        'Comedy': '喜剧', 'Mystery': '悬疑', 'Crime': '犯罪', 'Biography': '传记',
        'Fantasy': '奇幻', 'Documentary': '纪录片', 'Sci-Fi': '科幻', 'Romance': '爱情',
        'Family': '家庭', 'Horror': '恐怖', 'Thriller': '惊悚', 'Musical': '音乐',
        'Western': '西部', 'History': '历史', 'Sport': '运动', 'War': '战争'
    }
    df['Genre'] = df['Genre'].str.split('|').str[0].map(genre_map).fillna(df['Genre'])
    
    # 2.5 Rename columns to Chinese
    df.columns = ['电影', '类型', '成本', '票房', '评分', '导演', '年份']
    
    # 3. Cost/Revenue: 转换为"百万美元"单位，方便阅读
    df['成本'] = df['成本'] / 1000000
    df['票房'] = df['票房'] / 1000000
    
    # 4. Year: 转换为整数 (处理缺失值)
    df['年份'] = df['年份'].fillna(0).astype(int)
    
    # --- 保存完整数据集 (用于课后练习) ---
    # full_output_path = get_path('movies_dataset_full.xlsx')
    # df.to_excel(full_output_path, index=False)
    # print(f"Generated {full_output_path} with {len(df)} rows (Full Dataset).")
    
    # 4. 随机采样 500 条，保证包含一些特定类型的电影
    # 4. 随机采样 500 条，但要保证类型多样性
    # 我们从每个主要类型中抽取一些电影
    target_genres = ['动作', '冒险', '剧情', '喜剧', '爱情', '科幻', '悬疑', '动画']
    sampled_dfs = []
    
    for genre in target_genres:
        genre_df = df[df['类型'] == genre]
        if len(genre_df) > 0:
            # 每个类型最多取100部，最少取全部
            n_sample = min(len(genre_df), 100)
            sampled_dfs.append(genre_df.sample(n=n_sample, random_state=42))
            
    # 把剩下的类型也随机采一些
    other_genres_df = df[~df['类型'].isin(target_genres)]
    if len(other_genres_df) > 0:
        sampled_dfs.append(other_genres_df.sample(n=min(len(other_genres_df), 200), random_state=42))
        
    df = pd.concat(sampled_dfs).sample(frac=1, random_state=42).reset_index(drop=True)
    
    # 确保总数不超过 600
    if len(df) > 600:
        df = df.head(600)
    
    # --- 注入特定案例数据 (为了配合课件 Demo) ---
    # 1. 阿凡达 (Avatar) - 确保它存在且重复
    # 真实数据里可能已经有Avatar，我们先删掉，再手动加两个，确保状态可控
    # 1. 阿凡达 (Avatar) - 确保它存在且重复
    # 真实数据里可能已经有Avatar，我们先删掉，再手动加两个，确保状态可控
    df = df[df['电影'] != 'Avatar']
    avatar = pd.DataFrame([['Avatar', '动作', 237.0, 760.5, 7.9, 'James Cameron', 2009]], columns=df.columns)
    df = pd.concat([avatar, df, avatar], ignore_index=True) # 插入头部和中间
    
    # 2. 罗马假日 (Roman Holiday) - 用于演示缺失值
    # 真实数据里可能没有，手动加一个
    # 2. 罗马假日 (Roman Holiday) - 用于演示缺失值
    # 真实数据里可能没有，手动加一个。注意：为了不影响"爱情"类的均值计算，我们给它一个评分，但让票房为空
    roman = pd.DataFrame([['Roman Holiday', '爱情', 0, np.nan, 8.1, 'William Wyler', 1953]], columns=df.columns)
    df = pd.concat([df, roman], ignore_index=True)
    
    # --- 制造脏数据 (为了教学演示) ---
    # 1. 缺失成本 (Cost)
    mask_cost = np.random.choice(df.index, 20, replace=False)
    df.loc[mask_cost, '成本'] = np.nan
    
    # 2. 缺失评分 (Rating)
    mask_rating = np.random.choice(df.index, 10, replace=False)
    df.loc[mask_rating, '评分'] = np.nan
    
    output_path = get_path('movies.xlsx')
    df.to_excel(output_path, index=False)
    print(f"Generated {output_path} with {len(df)} rows using real IMDB data.")

if __name__ == "__main__":
    generate_hok_data()
    # generate_survey_data() # Lesson 3 旧数据，暂时保留或注释
    # generate_grades_data() # Lesson 4 旧数据，暂时保留或注释
    generate_movies_data()   # Lesson 3-4 新数据
