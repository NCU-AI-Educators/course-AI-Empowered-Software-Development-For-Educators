import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map, Bar, Pie, Page
from pyecharts.globals import ThemeType

# 1. 读取数据
DATA_PATH = "AI-Empowered-Software-Development-For-Educators/02-Lectures-And-Practices/module5/data/china_tourism.csv"
df = pd.read_csv(DATA_PATH)

# 简单的数据清洗：有些City是空的，填一下
df['City'] = df['City'].fillna('未知')

# --- 2. 准备图表数据 ---

# [地图数据] 统计各省的 5A 景区数量
# 注意：我们的csv只有City列，没有Province列。
# 为了演示，我们用一个简单的映射字典（这里只列出部分主要省份做演示，真实项目需要更全的映射）
# 或者我们简单粗暴一点：直接用City画散点地图（Geo），或者只画几个主要省份的Map。
# 为了效果震撼，我这里硬编码一个简易的 "City -> Province" 映射逻辑
# (实际教学中，这是可以让学员用 AI 完成的任务)

# 假设我们已经有了 Province 列 (如果没有，我们用 'City' 代替展示，虽然在 Map 上可能匹配不到，
# 但 pyecharts 的 Map 支持 'China' 模式下直接显示 '北京', '上海' 等直辖市和省份)
# 我们先统计 5A 景区最多的城市，用来模拟热力
top_cities_5a = df[df['Level'] == '5A']['City'].value_counts().head(20)
map_data = [list(z) for z in zip(top_cities_5a.index, top_cities_5a.values.tolist())]

# [柱状图数据] 热门城市 Top 10 (按景点总数)
top_cities_all = df['City'].value_counts().head(10)
bar_x = top_cities_all.index.tolist()
bar_y = top_cities_all.values.tolist()

# [饼图数据] 5A vs 4A 占比
level_counts = df['Level'].value_counts()
# 只取 5A, 4A, 3A
pie_data = []
for level in ['5A', '4A', '3A']:
    if level in level_counts:
        pie_data.append([level, int(level_counts[level])])

# --- 3. 构建图表 ---

# Map (中国地图 - 省份热力)
# 这里的逻辑是：为了演示，我们手动把 Top 城市映射到省份
city_to_province = {
    '北京': '北京', '上海': '上海', '重庆': '重庆', '天津': '天津',
    '西安': '陕西', '成都': '四川', '杭州': '浙江', '广州': '广东',
    '南京': '江苏', '三亚': '海南', '苏州': '浙江', '厦门': '福建',
    '青岛': '山东', '大理': '云南', '丽江': '云南', '桂林': '广西',
    '哈尔滨': '黑龙江', '武汉': '湖北', '长沙': '湖南', '昆明': '云南'
}

# 统计各省 5A 数量 (模拟)
province_counts = {}
df_5a = df[df['Level'] == '5A']
for city in df_5a['City']:
    prov = city_to_province.get(city) # 简单查表
    if prov:
        province_counts[prov] = province_counts.get(prov, 0) + 1

map_data = [list(z) for z in province_counts.items()]

c_map = (
    Map(init_opts=opts.InitOpts(theme=ThemeType.DARK, width="1000px", height="600px"))
    .add("5A景区数量", map_data, "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国旅游资源热力图 (Top城市示例)", pos_left="center"),
        visualmap_opts=opts.VisualMapOpts(max_=5),
    )
)

# Bar (热门城市)
c_bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(bar_x)
    .add_yaxis("景点数量", bar_y, itemstyle_opts=opts.ItemStyleOpts(color="#d48265"))
    .set_global_opts(title_opts=opts.TitleOpts(title="热门城市 Top 10"))
)

# Pie (等级占比)
c_pie = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add("", pie_data, radius=["30%", "75%"], rosetype="radius")
    .set_global_opts(title_opts=opts.TitleOpts(title="景区等级分布"))
)

# --- 4. 组合大屏 ---
page = Page(layout=Page.DraggablePageLayout, page_title="旅游数据驾驶舱")
page.add(c_map, c_bar, c_pie)

OUTPUT_PATH = "AI-Empowered-Software-Development-For-Educators/02-Lectures-And-Practices/module5/data/tourism_dashboard.html"
page.render(OUTPUT_PATH)

print(f"Dashboard generated at: {OUTPUT_PATH}")
