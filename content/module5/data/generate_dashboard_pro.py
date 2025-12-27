import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map, Bar, Pie, Page, Gauge
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode

# 1. 读取数据
DATA_PATH = "AI-Empowered-Software-Development-For-Educators/02-Lectures-And-Practices/module5/data/china_tourism.csv"
df = pd.read_csv(DATA_PATH)

# --- 数据准备 ---
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

# 地图数据
province_counts = {}
df_target = df 
for city in df_target['City']:
    clean_city = str(city).replace('市', '').strip()
    prov = city_to_province.get(clean_city)
    if prov:
        province_counts[prov] = province_counts.get(prov, 0) + 1
map_data = [list(z) for z in province_counts.items()]

# 柱状图数据
top_cities_price = df.groupby('City')['Sold_Price'].mean().sort_values(ascending=False).head(10)
bar_x = top_cities_price.index.tolist()
bar_y = [int(x) for x in top_cities_price.values]

# 饼图数据 (只含A级)
level_counts = df['Level'].value_counts()
valid_levels = ['5A', '4A', '3A', '2A', '1A']
pie_data = []
for level in valid_levels:
    if level in level_counts:
        pie_data.append([level, int(level_counts[level])])

# 仪表盘数据
avg_price = int(df[df['Sold_Price'] > 0]['Sold_Price'].mean())

# --- 3. UI 设计 (Tech Theme) ---
THEME = ThemeType.PURPLE_PASSION
# 关键：图表设为 100% 宽高，由外部 CSS Grid 控制容器大小
FULL_SIZE = opts.InitOpts(theme=THEME, width="100%", height="100%")

# 3.1 核心地图 (Hero Section)
c_map = (
    Map(init_opts=FULL_SIZE)
    .add(
        "景点热力", 
        map_data, 
        "china",
        is_map_symbol_show=False,
        label_opts=opts.LabelOpts(is_show=False),
        itemstyle_opts=opts.ItemStyleOpts(border_color="#111", border_width=1),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="中国旅游资源全景热力图", 
            pos_left="center", 
            pos_top="20px",
            title_textstyle_opts=opts.TextStyleOpts(font_size=24, color="#fff")
        ),
        visualmap_opts=opts.VisualMapOpts(
            max_=max(province_counts.values()) if province_counts else 100,
            is_piecewise=False,
            range_color=["#182642", "#28527a", "#37a2da", "#e0ffff", "#ffd700", "#ff4500", "#ff0000"],
            pos_left="5%",
            pos_bottom="10%",
            textstyle_opts=opts.TextStyleOpts(color="#fff")
        ),
        legend_opts=opts.LegendOpts(is_show=False)
    )
)

# 3.2 排行榜 (Ranking)
c_bar = (
    Bar(init_opts=FULL_SIZE)
    .add_xaxis(bar_x)
    .add_yaxis(
        "平均票价", 
        bar_y, 
        category_gap="40%",
        itemstyle_opts={
            "normal": {
                "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                    offset: 0,
                    color: '#00b4db'
                }, {
                    offset: 1,
                    color: '#0083b0'
                }], false)"""),
                "barBorderRadius": [0, 20, 20, 0],
            }
        }
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="城市平均票价 Top 10 (元)", pos_left="center", title_textstyle_opts=opts.TextStyleOpts(color="#fff")),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(color="#fff", font_size=12),
            axisline_opts=opts.AxisLineOpts(is_show=False),
            axistick_opts=opts.AxisTickOpts(is_show=False)
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="right", color="#fff"))
)

# 3.3 环形图 (Donut)
c_pie = (
    Pie(init_opts=FULL_SIZE)
    .add(
        "", 
        pie_data, 
        radius=["40%", "60%"], 
        center=["50%", "55%"],
        rosetype="radius",
        label_opts=opts.LabelOpts(is_show=True, formatter="{b}: {c} ({d}%)", color="#fff"), 
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="A级景区等级分布 (不含无评级)", pos_left="center", title_textstyle_opts=opts.TextStyleOpts(color="#fff", font_size=14)),
        legend_opts=opts.LegendOpts(type_="scroll", pos_bottom="5%", textstyle_opts=opts.TextStyleOpts(color="#fff"))
    )
)

# 3.4 仪表盘 (Gauge)
c_gauge = (
    Gauge(init_opts=FULL_SIZE)
    .add(
        "平均票价",
        [("全网均价", avg_price)],
        min_=0, max_=300,
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[[0.3, "#67e0e3"], [0.7, "#37a2da"], [1, "#fd666d"]], width=15
            )
        ),
        axislabel_opts=opts.LabelOpts(color="#fff"),
        title_label_opts=opts.LabelOpts(color="#fff", font_size=16),
        detail_label_opts=opts.LabelOpts(formatter="¥{value}", font_size=24, color="#00eaff", font_weight="bold")
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="", pos_left="center"))
)

# --- 4. 生成 HTML ---
page = Page(layout=Page.SimplePageLayout, page_title="旅游大数据驾驶舱")
# 这里的顺序很重要，对应 CSS nth-child
# 1: Bar, 2: Map, 3: Gauge, 4: Pie
page.add(c_bar, c_map, c_gauge, c_pie)

OUTPUT_PATH = "AI-Empowered-Software-Development-For-Educators/02-Lectures-And-Practices/module5/data/tourism_dashboard_pro.html"
page.render(OUTPUT_PATH)

# --- 5. 注入 CSS Grid ---
with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
    content = f.read()

css_style = """
<style>
    body {
        background-color: #100c2a; 
        margin: 0; 
        padding: 20px;
        font-family: "Microsoft YaHei", sans-serif;
        height: 100vh;
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
    }
    h1 {
        color: #fff;
        text-align: center;
        margin: 0 0 20px 0;
        text-shadow: 0 0 10px #00eaff;
        flex: 0 0 auto;
    }
    
    /* Grid 容器 */
    #dashboard-grid {
        display: grid;
        /* 左侧 30%, 右侧 70% */
        grid-template-columns: 30% 70%; 
        /* 上层 60%, 下层 40% (大概比例，根据内容调整) */
        grid-template-rows: 60% 40%;
        gap: 20px;
        flex: 1 1 auto;
        height: 0; /* 强制填满剩余空间 */
    }
    
    /* 通用卡片样式 */
    .chart-container {
        width: 100% !important;
        height: 100% !important;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        padding: 10px;
        overflow: hidden; /* 防止溢出 */
    }

    /* 布局分配 */
    /* 1. Bar (左上) */
    #dashboard-grid > div:nth-child(1) { 
        grid-row: 1 / 2; 
        grid-column: 1 / 2; 
    }
    
    /* 2. Map (右上 - 跨两行? 或者只占右上) */
    /* 方案：Map 占据右上，Pie 占据右下 */
    #dashboard-grid > div:nth-child(2) { 
        grid-row: 1 / 3;  /* Map 占据右侧全高，作为视觉中心 */
        grid-column: 2 / 3; 
    }
    
    /* 3. Gauge (左下) */
    #dashboard-grid > div:nth-child(3) { 
        grid-row: 2 / 3; 
        grid-column: 1 / 2; 
        /* 分两列放 Gauge 和 Pie? 不，Gauge自己占左下 */
    }
    
    /* 4. Pie (原本在右下，现在没地方了？) */
    /* 等等，如果 Map 占满右侧，Pie 放哪？*/
    /* 修改布局：Map 占右上，Pie 占右下 */
    
    #dashboard-grid > div:nth-child(2) { 
        grid-row: 1 / 2;  /* Map 只占右上 */
        grid-column: 2 / 3; 
    }
    
    #dashboard-grid > div:nth-child(4) { 
        grid-row: 2 / 3;  /* Pie 占右下 */
        grid-column: 2 / 3; 
    }
    
    /* 调整一下高度比例，让 Map 更大 */
    #dashboard-grid {
        grid-template-rows: 65% 35%;
    }

</style>
"""

new_content = content.replace('<body>', f'{css_style}<body><h1>🇨🇳 中国旅游大数据驾驶舱</h1><div id="dashboard-grid">')
new_content = new_content.replace('</body>', '</div></body>')

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Pro Dashboard generated at: {OUTPUT_PATH}")