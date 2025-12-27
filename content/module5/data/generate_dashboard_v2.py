import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map, Bar, Pie, Page, Gauge, Grid
from pyecharts.globals import ThemeType, ChartType, SymbolType

# 1. 读取数据
DATA_PATH = "AI-Empowered-Software-Development-For-Educators/02-Lectures-And-Practices/module5/data/china_tourism.csv"
df = pd.read_csv(DATA_PATH)

# --- 2. 数据增强：全量城市-省份映射 ---
# 为了确保地图不空，我们需要一个覆盖主要城市的映射表
# Pyecharts Map 需要标准全称
city_to_province = {
    '北京': '北京市', '上海': '上海市', '天津': '天津市', '重庆': '重庆市',
    '哈尔滨': '黑龙江省', '齐齐哈尔': '黑龙江省', '牡丹江': '黑龙江省', '佳木斯': '黑龙江省', '大庆': '黑龙江省',
    '长春': '吉林省', '吉林': '吉林省', '延边': '吉林省', '四平': '吉林省',
    '沈阳': '辽宁省', '大连': '辽宁省', '鞍山': '辽宁省', '丹东': '辽宁省', '锦州': '辽宁省',
    '呼和浩特': '内蒙古自治区', '包头': '内蒙古自治区', '赤峰': '内蒙古自治区', '鄂尔多斯': '内蒙古自治区', '呼伦贝尔': '内蒙古自治区',
    '石家庄': '河北省', '唐山': '河北省', '秦皇岛': '河北省', '邯郸': '河北省', '保定': '河北省', '张家口': '河北省', '承德': '河北省',
    '太原': '山西省', '大同': '山西省', '晋中': '山西省', '临汾': '山西省', '运城': '山西省',
    '济南': '山东省', '青岛': '山东省', '淄博': '山东省', '烟台': '山东省', '潍坊': '山东省', '济宁': '山东省', '泰安': '山东省', '威海': '山东省',
    '南京': '江苏省', '无锡': '江苏省', '徐州': '江苏省', '常州': '江苏省', '苏州': '江苏省', '南通': '江苏省', '连云港': '江苏省', '扬州': '江苏省',
    '杭州': '浙江省', '宁波': '浙江省', '温州': '浙江省', '嘉兴': '浙江省', '湖州': '浙江省', '绍兴': '浙江省', '金华': '浙江省', '舟山': '浙江省', '台州': '浙江省',
    '合肥': '安徽省', '芜湖': '安徽省', '蚌埠': '安徽省', '黄山': '安徽省', '安庆': '安徽省',
    '福州': '福建省', '厦门': '福建省', '莆田': '福建省', '三明': '福建省', '泉州': '福建省', '漳州': '福建省', '南平': '福建省', '龙岩': '福建省',
    '南昌': '江西省', '景德镇': '江西省', '九江': '江西省', '赣州': '江西省', '吉安': '江西省', '宜春': '江西省', '上饶': '江西省',
    '郑州': '河南省', '开封': '河南省', '洛阳': '河南省', '安阳': '河南省', '焦作': '河南省', '南阳': '河南省', '信阳': '河南省',
    '武汉': '湖北省', '黄石': '湖北省', '十堰': '湖北省', '宜昌': '湖北省', '襄阳': '湖北省', '恩施': '湖北省', '神农架': '湖北省',
    '长沙': '湖南省', '株洲': '湖南省', '湘潭': '湖南省', '衡阳': '湖南省', '张家界': '湖南省', '郴州': '湖南省', '湘西': '湖南省',
    '广州': '广东省', '韶关': '广东省', '深圳': '广东省', '珠海': '广东省', '汕头': '广东省', '佛山': '广东省', '江门': '广东省', '湛江': '广东省', '惠州': '广东省', '东莞': '广东省', '中山': '广东省',
    '南宁': '广西壮族自治区', '柳州': '广西壮族自治区', '桂林': '广西壮族自治区', '北海': '广西壮族自治区',
    '海口': '海南省', '三亚': '海南省', '三沙': '海南省', '儋州': '海南省',
    '成都': '四川省', '自贡': '四川省', '攀枝花': '四川省', '泸州': '四川省', '德阳': '四川省', '绵阳': '四川省', '广元': '四川省', '乐山': '四川省', '南充': '四川省', '宜宾': '四川省', '阿坝': '四川省', '甘孜': '四川省', '凉山': '四川省',
    '贵阳': '贵州省', '遵义': '贵州省', '安顺': '贵州省', '黔西南': '贵州省', '黔东南': '贵州省', '黔南': '贵州省',
    '昆明': '云南省', '曲靖': '云南省', '玉溪': '云南省', '保山': '云南省', '丽江': '云南省', '普洱': '云南省', '临沧': '云南省', '楚雄': '云南省', '红河': '云南省', '文山': '云南省', '西双版纳': '云南省', '大理': '云南省', '德宏': '云南省', '迪庆': '云南省',
    '拉萨': '西藏自治区', '日喀则': '西藏自治区', '林芝': '西藏自治区',
    '西安': '陕西省', '宝鸡': '陕西省', '咸阳': '陕西省', '渭南': '陕西省', '延安': '陕西省', '汉中': '陕西省', '榆林': '陕西省',
    '兰州': '甘肃省', '嘉峪关': '甘肃省', '天水': '甘肃省', '张掖': '甘肃省', '酒泉': '甘肃省', '庆阳': '甘肃省', '甘南': '甘肃省',
    '西宁': '青海省', '海北': '青海省',
    '银川': '宁夏回族自治区', '中卫': '宁夏回族自治区',
    '乌鲁木齐': '新疆维吾尔自治区', '吐鲁番': '新疆维吾尔自治区', '哈密': '新疆维吾尔自治区', '昌吉': '新疆维吾尔自治区', '博尔塔拉': '新疆维吾尔自治区', '巴音郭楞': '新疆维吾尔自治区', '阿克苏': '新疆维吾尔自治区', '喀什': '新疆维吾尔自治区', '和田': '新疆维吾尔自治区', '伊犁': '新疆维吾尔自治区', '阿勒泰': '新疆维吾尔自治区'
}

# 统计各省 5A 景区
province_counts = {}
# 这里我们只统计 Level 为 5A 的，数据会更稀疏但更真实；或者统计所有景点
df_target = df # 统计所有景点，热力会更满
for city in df_target['City']:
    # 清洗城市名（去掉“市”后缀，提高匹配率）
    clean_city = str(city).replace('市', '').strip()
    prov = city_to_province.get(clean_city)
    if prov:
        province_counts[prov] = province_counts.get(prov, 0) + 1

map_data = [list(z) for z in province_counts.items()]
print("Debug - Map Data Sample:", map_data[:5]) # 调试打印

# --- 3. 关键指标计算 ---
total_spots = len(df)
avg_price = int(df[df['Sold_Price'] > 0]['Sold_Price'].mean())

# [修复柱状图]
# 原始数据每个城市固定100条，所以计数没意义。改为计算“平均门票价格”
top_cities_price = df.groupby('City')['Sold_Price'].mean().sort_values(ascending=False).head(10)
bar_x = top_cities_price.index.tolist()
# 转换为整数，保留一位小数也可
bar_y = [int(x) for x in top_cities_price.values]
print("Debug - Bar Data Y (Price):", bar_y) # 调试打印

# --- 4. 构建图表 (使用 PURPLE_PASSION 主题) ---
THEME = ThemeType.PURPLE_PASSION

# 4.1 地图 (核心)
# Pyecharts Map 通常识别简称（如 '广东', '北京'）。我们的 city_to_province 已经是简称了。
c_map = (
    Map(init_opts=opts.InitOpts(theme=THEME, width="48%", height="400px")) # 宽度 48% 以便并排
    .add(
        "景点数量", 
        map_data, 
        "china",
        is_map_symbol_show=False,
        label_opts=opts.LabelOpts(is_show=True, color="#fff"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国旅游资源热力分布", pos_left="center"),
        visualmap_opts=opts.VisualMapOpts(
            # 动态设置最大值，防止全白。因为有的大省1000+，设置500可以让大部分省份都有颜色
            max_=500,
            range_color=["#313695", "#4575b4", "#74add1", "#abd9e9", "#e0f3f8", "#ffffbf", "#fee090", "#fdae61", "#f46d43", "#d73027", "#a50026"],
        ),
    )
)

# 4.2 柱状图 (Top 10 价格)
c_bar = (
    Bar(init_opts=opts.InitOpts(theme=THEME, width="48%", height="400px"))
    .add_xaxis(bar_x)
    .add_yaxis("平均门票", bar_y, itemstyle_opts=opts.ItemStyleOpts(color="#d48265"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="热门城市平均门票价格 Top 10", pos_left="center"),
        legend_opts=opts.LegendOpts(is_show=False)
    )
)

# 4.3 饼图 (等级分布)
level_counts = df['Level'].value_counts()

# 只保留合法的 A 级景区 (5A - 1A)，忽略无评级，以保证图表重点突出
valid_levels = ['5A', '4A', '3A', '2A', '1A']
pie_data = []
for level in valid_levels:
    if level in level_counts:
        pie_data.append([level, int(level_counts[level])])

c_pie = (
    Pie(init_opts=opts.InitOpts(theme=THEME, width="48%", height="300px"))
    .add(
        "", 
        pie_data, 
        radius=["40%", "70%"], 
        center=["50%", "50%"],
        rosetype="radius"
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="A级景区等级分布 (不含无评级)", pos_left="left"),
        legend_opts=opts.LegendOpts(pos_right="right", orient="vertical")
    )
)

# 4.4 仪表盘 (核心KPI - 平均票价)
c_gauge = (
    Gauge(init_opts=opts.InitOpts(theme=THEME, width="48%", height="300px"))
    .add(
        "平均票价",
        [("元", avg_price)],
        min_=0, max_=300,
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[[0.3, "#67e0e3"], [0.7, "#37a2da"], [1, "#fd666d"]], width=30
            )
        ),
        detail_label_opts=opts.LabelOpts(formatter="{value}"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="全国景点平均门票价格", pos_left="center", pos_top="20px"))
)

# --- 5. 组合大屏 ---
# 使用 SimplePageLayout 自动流式布局
page = Page(layout=Page.SimplePageLayout, page_title="旅游大数据驾驶舱")
page.add(
    c_map, c_bar,  # 第一行：地图 + 柱状图
    c_gauge, c_pie # 第二行：仪表盘 + 饼图
)

OUTPUT_PATH = "AI-Empowered-Software-Development-For-Educators/02-Lectures-And-Practices/module5/data/tourism_dashboard_v2.html"
page.render(OUTPUT_PATH)

print(f"Dashboard generated at: {OUTPUT_PATH}")
