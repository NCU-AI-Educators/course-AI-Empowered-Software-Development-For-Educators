# 《AI赋能软件开发》课程高级挑战项目

## 引言

欢迎来到挑战区！

本文档专为已经掌握课程基础内容, 并渴望探索更广阔AI应用场景的学员设计. 这里的每一个项目都对应着一个真实的工业界需求, 它们会比基础项目更复杂, 但带来的回报和成就感也将是巨大的.

请将这些项目视为你展示综合能力的舞台. 在解决这些挑战时, 请尽情地, 大胆地向你的AI编程助手提问, 指挥它完成你想要的任何功能. 祝你探索愉快!

---

## 挑战项目一: 交互式小说/文本冒险游戏引擎 (武侠MUD怀旧版)

- **对应模块**: 模块二 (与AI对话)
- **项目背景**: 在图形化网络游戏诞生之前, MUD(Multi-User Dungeon, 多人地下城)是风靡全球的网络游戏鼻祖. 在那个计算能力有限的时代, 玩家通过纯文本指令与世界互动. 在中国, 最受欢迎的MUD主题便是**武侠**, 玩家们通过输入`go north`, `kill monster`, 甚至 `perform liumai-shenjian` (使用六脉神剑)等指令, 在一个文字构建的江湖里快意恩仇. 本项目旨在复刻这种经典的游戏模式, 让你亲手构建一个属于自己的迷你武侠世界.

### 核心挑战

1.  **数据结构化**: 学会如何用嵌套的字典(Dictionary)来描述一个世界(地图, 房间, NPC).
2.  **状态管理**: 理解并维护一个"游戏状态", 核心是玩家的"当前位置".
3.  **指令解析**: 编写一个能理解玩家输入的简单"解析器", 将"go east"这样的指令分解为程序可以理解的动作.
4.  **游戏循环**: 实现一个持续运行, 不断接收输入并更新状态的"主循环".

### 技术栈建议

- 纯Python! 仅使用`字典`, `列表`, `while循环`, `if/else判断`等最基础的语法.

### 实现步骤指引

这是一个纯逻辑的Python程序, 非常适合锻炼你的结构化思维. 你可以把下面的代码框架交给AI, 让它帮你解释并填充`TODO`部分, 或者增加更多有趣的地点和指令.

```python
# --- 1. 定义你的武侠世界 ---
# 我们使用一个“字典的字典”来结构化地描述整个游戏世界.
# 外层字典的键 (如 'guangchang') 是每个地点的唯一ID.
# 内层字典则包含了该地点的所有属性, 如描述和出口.
world = {
    'guangchang': {
        'description': '你正站在扬州城的中央广场, 人来人往, 叫卖声不绝于耳. 东边是一家茶馆, 西边是兵器铺.',
        'exits': {'east': 'chaguan', 'west': 'bingqipu'} # 'exits' 的值也是一个字典, 定义了从这里可以去往的方向和目标地点的ID.
    },
    'chaguan': {
        'description': '你走进了一家茶馆, 店小二热情地迎了上来: “客官, 喝点什么?” 广场在你的西边.',
        'exits': {'west': 'guangchang'}
    },
    'bingqipu': {
        'description': '这里是兵器铺, 墙上挂着各式各样的刀剑. 一位老师傅正在打铁. 广场在你的东边.',
        'exits': {'east': 'guangchang'}
    }
}

# --- 2. 初始化游戏状态 ---
# 使用一个变量来追踪玩家的当前位置. 它的值就是 world 字典中某个地点的ID.
current_location_id = 'guangchang'

# --- 3. 游戏主循环 ---
# while True 创建了一个无限循环, 使得游戏可以持续接收玩家的指令, 直到玩家选择退出.
print("--- 欢迎来到迷你武侠世界! ---\n你可以使用的指令有: go [方向], look, quit")

while True:
    # a. 获取当前地点的信息: 基于玩家的当前位置ID, 从 world 字典中获取该地点的详细数据.
    current_location_data = world[current_location_id]
    
    # b. 打印当前地点的描述: 将当前位置的描述信息展示给玩家.
    print("\n" + "- " * 15)
    print(current_location_data['description'])
    
    # c. 获取用户输入: 程序在此暂停, 等待玩家输入指令. .lower() 将输入转为小写, .strip() 去除首尾空格, 方便后续判断.
    command = input("> ").lower().strip()
    
    # d. 解析并执行指令: 这是游戏的核心逻辑部分.
    if command == 'quit':
        print("\n你退出了江湖...\n")
        break # break 语句会跳出当前的 while 循环, 从而结束游戏. 
    
    if command == 'look':
        # 'look' 指令的目的是重新观察当前环境. 在我们的循环结构中, 每次循环开始时都会打印环境描述.
        # 因此, 这里使用 continue 跳过本次循环的余下部分, 直接进入下一次循环, 就会自动重新打印描述.
        continue

    # 将玩家输入的指令按空格分割成一个列表, 例如 'go east' 会变成 ['go', 'east'].
    parts = command.split() 
    if len(parts) == 2 and parts[0] == 'go':
        direction = parts[1]
        # 检查玩家想去的方向是否存在于当前地点的 'exits' 字典中.
        if direction in current_location_data['exits']:
            # 如果方向有效, 就更新玩家的当前位置ID.
            current_location_id = current_location_data['exits'][direction]
        else:
            print(f"你不能往 {direction} 方向走.")
    else:
        # 如果指令不满足任何已知的格式, 就提示玩家输入无效.
        print("无效的指令. (试试: go east, look, quit)")

    # TODO: 指挥AI帮你增加更多指令, 比如 'look npc', 'take item', 甚至 'fight'!

```

---

## 挑战项目二: 终极文件批量重命名工具

- **对应模块**: 模块三 (自动化的魔力)
- **项目背景**: 在日常工作和学习中, 我们经常需要批量处理文件, 例如将仪器采集到的**实验数据文件**, 显微镜拍摄的**实验图像文件**, 或下载的**网课视频**等进行统一格式的重命名. 一个强大而灵活的批量重命名工具能极大地提升效率.

### 核心挑战

1.  **复杂逻辑与UI分离**: 设计清晰的后端函数来处理不同的重命名逻辑.
2.  **动态UI交互**: 根据用户选择的重命名模式, 动态显示或隐藏不同的设置选项.
3.  **预览与安全**: 在实际执行重命名操作前, 提供一个"预览"功能, 防止误操作. 这是一个优秀工具必备的人性化设计.

### 技术栈建议

- `os`, `re` (正则表达式), `datetime`, `Gradio`

### 实现步骤指引

这是一个包含动态UI和预览功能的完整Gradio应用框架. 请把它交给AI, 让它帮你解释和实现每个`TODO`部分.

```python
import gradio as gr
import os
import re
from datetime import datetime

# --- 1. 核心后端逻辑 ---
# 将核心功能 (文件重命名) 与用户界面 (Gradio) 分离, 是良好的软件设计实践.

def preview_rename(directory, mode, prefix, start_num_str, pattern, replacement):
    """
    根据用户选择的模式和参数, 生成文件重命名的预览.
    这个函数不执行任何实际的文件操作, 只是返回一个预览列表.
    """
    if not os.path.isdir(directory):
        return [], "错误: 文件夹不存在"
    
    try:
        # 1. 获取并排序文件夹下的所有文件名
        files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
        preview_data = []
        start_num = int(start_num_str)
        
        # 2. 遍历每个文件, 根据重命名模式生成新文件名
        for i, old_name in enumerate(files):
            new_name = ""
            # TODO: 指挥AI根据不同的mode, 计算出new_name
            if mode == "添加前缀":
                new_name = f"{prefix}{old_name}"
            elif mode == "序列化重命名":
                # .zfill(3) 用于补零, 例如将 '1' 变成 '001'
                ext = os.path.splitext(old_name)[1] # 分离文件名和扩展名
                new_name = f"{prefix}{str(i + start_num).zfill(3)}{ext}"
            elif mode == "正则替换":
                # re.sub 是正则表达式库中的替换函数
                new_name = re.sub(pattern, replacement, old_name)
            elif mode == "修改时间重命名":
                # 获取文件的最后修改时间, 并格式化为字符串
                mtime = os.path.getmtime(os.path.join(directory, old_name))
                mtime_str = datetime.fromtimestamp(mtime).strftime('%Y%m%d_%H%M%S')
                new_name = f"{mtime_str}_{old_name}"
            
            if new_name:
                preview_data.append([old_name, new_name])
                
        # 3. 返回预览数据和成功消息
        return preview_data, "预览生成成功!"
    except Exception as e:
        return [], f"错误: {e}"

def execute_rename(directory, preview_data):
    """
    根据预览数据, 实际执行文件重命名操作.
    """
    if not preview_data:
        return "错误: 没有可执行的重命名操作."
    
    count = 0
    for old_name, new_name in preview_data:
        try:
            # os.rename 是一个危险操作, 因此预览功能至关重要
            os.rename(os.path.join(directory, old_name), os.path.join(directory, new_name))
            count += 1
        except Exception as e:
            return f"在重命名 '{old_name}' 时出错: {e}"
    return f"成功重命名 {count} 个文件!"

# --- 2. 构建Gradio界面 ---
# gr.Blocks() 提供了一个灵活的方式来组合和布局Gradio组件.
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 终极文件批量重命名工具")
    
    with gr.Row():
        dir_input = gr.Textbox(label="要操作的文件夹路径")
        rename_mode_dd = gr.Dropdown(["添加前缀", "序列化重命名", "修改时间重命名", "正则替换"], label="重命名模式")

    # --- 动态UI ---
    # 创建多个选项区域, 但默认只显示第一个.
    # `visible=False` 参数让这些区域在初始时隐藏.
    with gr.Column() as prefix_options:
        prefix_input = gr.Textbox(label="前缀", value="MyPrefix_")
    with gr.Column(visible=False) as sequential_options:
        seq_prefix_input = gr.Textbox(label="序列前缀", value="file_")
        start_num_input = gr.Textbox(label="起始编号", value="1")
    with gr.Column(visible=False) as regex_options:
        pattern_input = gr.Textbox(label="正则表达式模式")
        replacement_input = gr.Textbox(label="替换内容")
    
    # 预览和执行按钮
    preview_btn = gr.Button("生成预览", variant="secondary")
    execute_btn = gr.Button("执行重命名!", variant="primary")
    status_output = gr.Textbox(label="状态", interactive=False)
    
    # 预览表格: Dataframe组件非常适合用于显示表格数据.
    preview_table = gr.Dataframe(headers=["原始文件名", "新文件名"], label="重命名预览", interactive=False)

    # --- 3. 设定组件之间的联动关系 ---
    # 这是Gradio实现动态UI的核心.
    def update_ui_visibility(mode):
        # TODO: 指挥AI帮你实现这个函数, 根据选择的模式, 返回不同UI组件的可见性
        # 这个函数返回一个元组, 每个元素都对应一个 output 组件的更新.
        # gr.update(visible=...) 可以改变组件的可见性.
        return (
            gr.update(visible=mode=="添加前缀"),
            gr.update(visible=mode=="序列化重命名"),
            gr.update(visible=mode=="正则替换")
        )
    
    # .change() 方法将一个函数绑定到组件的“值改变”事件上.
    # 当 `rename_mode_dd` 的值改变时, `update_ui_visibility` 函数会被调用.
    # `inputs` 定义了哪些组件的值会作为参数传给函数.
    # `outputs` 定义了哪些组件会被函数的返回值所更新.
    rename_mode_dd.change(fn=update_ui_visibility, inputs=rename_mode_dd, outputs=[prefix_options, sequential_options, regex_options])
    
    # .click() 方法将一个函数绑定到按钮的“点击”事件上.
    preview_btn.click(
        fn=preview_rename,
        inputs=[dir_input, rename_mode_dd, prefix_input, start_num_input, pattern_input, replacement_input],
        outputs=[preview_table, status_output]
    )
    
    execute_btn.click(
        fn=execute_rename,
        inputs=[dir_input, preview_table],
        outputs=[status_output]
    )

# --- 4. 启动应用 ---
demo.launch()
```

---

## 挑战项目三: 个人知识库索引与检索工具

- **对应模块**: 模块三 (自动化的魔力)
- **项目背景**: 随着你电脑中的文档越来越多, 通过手动翻找或者简单的文件名搜索已经难以高效地定位信息. 本项目旨在构建一个工具来**索引**你的个人文件, 实现基于内容的快速检索.

### 核心挑战

1.  **构建索引与检索逻辑**: 设计并实现一个能够扫描文件系统, 读取文件内容, 并根据关键词建立内存索引的核心逻辑.
2.  **构建多级联动UI**: 创建一个包含"构建索引 -> 选择关键词 -> 显示文件列表 -> 查看文件"这样多步骤交互逻辑的Web应用.

### 技术栈建议

- `os`, `Gradio`

### 实现步骤指引

```python
import gradio as gr
import os

# --- 1. 全局状态定义 ---
# 使用一个全局变量来存储文件索引. 这是一个简化的做法, 在真实的大型应用中可能会使用数据库或更专业的索引文件.
# 索引的结构是: { "关键词": ["文件路径1", "文件路径2", ...], ... }
file_index = {}

# --- 2. 核心功能函数 ---
def build_index(directory, keywords_str):
    """
    遍历指定目录下的所有文件, 根据关键词构建或更新内存中的 `file_index`.
    """
    global file_index # 声明我们将要修改全局变量 file_index
    file_index = {} # 每次重建索引时都清空旧的索引
    keywords = [k.strip() for k in keywords_str.split(',') if k.strip()]
    
    if not directory or not os.path.isdir(directory):
        return "错误: 请提供一个有效的文件夹路径", gr.update(choices=[], value=None)
        
    indexed_files_count = 0
    # os.walk() 是一个非常有用的函数, 它可以递归地遍历一个目录下的所有子目录和文件.
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # 读取文件内容. 'errors=ignore' 会忽略解码错误, 防止因少量二进制文件而中断程序.
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                # 检查每个关键词是否存在于文件内容中
                for keyword in keywords:
                    if keyword in content:
                        # 如果关键词是第一次出现, 在索引中为它创建一个新列表
                        if keyword not in file_index:
                            file_index[keyword] = []
                        # 将包含该关键词的文件路径添加到索引中 (避免重复添加)
                        if file_path not in file_index[keyword]:
                            file_index[keyword].append(file_path)
                            indexed_files_count += 1
            except Exception:
                # 忽略读取单个文件时可能发生的任何错误 (如权限问题)
                pass
                
    status = f"索引构建完成! 共找到 {len(file_index)} 个关键词, 涉及 {indexed_files_count} 个文件."
    # 函数不仅返回状态信息, 还通过 gr.update() 来更新Gradio组件的属性.
    # 这里我们更新了关键词下拉菜单的选项.
    return status, gr.update(choices=list(file_index.keys()), value=None)

def update_file_list(selected_keyword):
    """
    当用户从下拉菜单中选择一个关键词时, 这个函数会被调用.
    它会根据所选的关键词, 更新文件列表单选框的选项.
    """
    if selected_keyword in file_index:
        return gr.update(choices=file_index[selected_keyword], value=None)
    return gr.update(choices=[], value=None)

def show_file_content(selected_file):
    """
    当用户从文件列表中选择一个文件时, 这个函数会被调用.
    它会读取并显示所选文件的内容.
    """
    if selected_file and os.path.exists(selected_file):
        with open(selected_file, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    return "请先选择一个文件"

# --- 3. 构建Gradio界面 ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 个人知识库索引与检索工具\n1. 输入要扫描的文件夹路径和关键词. \n2. 点击构建索引. \n3. 从下拉菜单选择关键词, 查看相关文件.")
    
    with gr.Row():
        dir_input = gr.Textbox(label="要索引的文件夹路径")
        keywords_input = gr.Textbox(label="关键词 (用逗号分隔)", value="软件工程, Python, Gradio")
        index_btn = gr.Button("构建/更新索引", variant="primary")
        
    status_output = gr.Textbox(label="状态", interactive=False)
    
    with gr.Row():
        keyword_dd = gr.Dropdown(label="选择关键词查看文件")
        file_list_radio = gr.Radio(label="包含该关键词的文件列表")
        
    file_content_output = gr.Textbox(label="文件内容", lines=20, interactive=False)

    # --- 4. 设定组件联动 ---
    # 整个应用的核心交互逻辑通过这三个 .click() 和 .change() 事件串联起来.
    # 1. 点击 "构建/更新索引" 按钮
    index_btn.click(fn=build_index, inputs=[dir_input, keywords_input], outputs=[status_output, keyword_dd])
    
    # 2. 当 "选择关键词" 下拉菜单的值改变时
    keyword_dd.change(fn=update_file_list, inputs=keyword_dd, outputs=file_list_radio)
    
    # 3. 当 "文件列表" 单选框的值改变时
    file_list_radio.change(fn=show_file_content, inputs=file_list_radio, outputs=file_content_output)

demo.launch()
```

---

## 挑战项目四: 一键生成“探索性数据分析(EDA)”报告

- **对应模块**: 模块四 (AI数据分析师-数据处理)
- **项目背景**: 在拿到一份新的数据集后, 专业的数据分析师通常会先进行探索性数据分析(EDA), 以了解数据的基本情况, 如每列的分布, 是否有缺失值, 列与列之间的相关性等. 这个过程虽然重要但很繁琐. 本项目将利用强大的第三方库, 实现"一键"生成图文并茂的专业EDA报告.

### 核心挑战

1.  **学习使用第三方库**: 引入并使用一个强大的自动化分析工具`ydata-profiling`.
2.  **报告解读**: 学会阅读和理解生成的专业分析报告, 并从中找出有价值的信息, 例如识别出数据中的潜在异常值或强相关性.
3.  **能力封装**: 将这个强大的分析能力封装成一个简单的Web应用, 任何人都可以上传数据并生成报告.

### 技术栈建议

- `pandas`: 用于读取数据.
- `ydata-profiling`: 用于生成报告.
- `Gradio`: 用于构建Web界面.

### 实现步骤指引

```python
import gradio as gr
import pandas as pd
from ydata_profiling import ProfileReport
import os

# --- 1. 核心功能函数 ---
def generate_eda_report(csv_file):
    """
    接收一个上传的CSV文件, 使用 ydata-profiling 生成EDA报告, 并返回HTML内容.
    """
    if csv_file is None:
        return None, "请先上传一个CSV文件."
    
    try:
        # 1. 使用pandas读取CSV文件
        # Gradio的UploadButton上传的文件是一个临时文件对象, .name 属性包含了它的路径.
        df = pd.read_csv(csv_file.name)
        
        # 2. 调用 ydata-profiling 生成报告
        # 这是本项目的核心, ProfileReport 接收一个pandas DataFrame, 并自动进行全面的探索性数据分析.
        profile = ProfileReport(df, title=f"{os.path.basename(csv_file.name)} 分析报告", explorative=True)
        
        # 3. 将报告保存为HTML文件
        output_path = "eda_report.html"
        profile.to_file(output_path)
        
        # 4. 读取HTML文件内容, 以便在Gradio中显示
        # Gradio的HTML组件可以直接渲染HTML字符串.
        with open(output_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        return html_content, f"报告已生成! 文件保存在: {output_path}"
    except Exception as e:
        return None, f"生成报告时出错: {e}"

# --- 2. 构建Gradio界面 ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 一键生成探索性数据分析(EDA)报告\n上传一个CSV文件, 点击按钮即可生成详细的数据分析报告.")
    
    with gr.Row():
        # UploadButton 允许用户上传文件, file_types 参数可以限制文件类型.
        upload_button = gr.UploadButton("上传CSV文件", file_types=[".csv"])
        generate_btn = gr.Button("生成分析报告", variant="primary")
    
    status_output = gr.Textbox(label="状态", interactive=False)
    # HTML 组件用于在Gradio界面中直接渲染和显示HTML内容.
    report_output = gr.HTML(label="分析报告预览")

    # --- 3. 设定组件之间的联动关系 ---
    generate_btn.click(
        fn=generate_eda_report,
        inputs=[upload_button],
        outputs=[report_output, status_output]
    )

# --- 4. 启动应用 ---
demo.launch()
```

---

## 挑战项目五: 交互式数据分析看板

- **对应模块**: 模块五 (AI数据分析师)
- **项目背景**: 你已经学会了如何从一个固定的CSV文件中生成图表. 现在, 你希望制作一个通用的Web应用, 允许任何人上传自己的CSV文件, 并通过点击鼠标来选择不同的列和图表类型, 动态地生成数据可视化结果.

### 核心挑战

从处理"静态"数据和需求, 升级到响应"动态"的用户输入和数据源.

### 技术栈建议

- `pandas`, `matplotlib`, `seaborn`, `Gradio`

### 实现步骤指引

```python
import gradio as gr
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_plot(csv_file, x_col, y_col, plot_type):
    """
    核心绘图函数. 它接收上传的文件和用户的选择, 然后使用matplotlib和seaborn生成图表.
    这个函数的设计体现了Gradio的“响应式”特性.
    """
    # 1. 处理初始状态或文件未上传的情况
    if csv_file is None:
        # 当没有文件时, 图表区域应为空, 同时清空下拉菜单的选项.
        return None, gr.Dropdown.update(choices=[], value=None), gr.Dropdown.update(choices=[], value=None)
    
    try:
        # 2. 读取数据并填充下拉菜单
        df = pd.read_csv(csv_file.name)
        columns = df.columns.tolist()
        
        # 3. 检查用户选择的列是否有效, 如果无效 (例如, 在新文件上传后), 则不绘图,只更新下拉菜单选项.
        if x_col not in columns or y_col not in columns:
            return None, gr.Dropdown.update(choices=columns), gr.Dropdown.update(choices=columns)
            
        # 4. 根据用户选择的图表类型, 使用seaborn进行绘图
        fig, ax = plt.subplots() # 创建一个新的matplotlib图表
        if plot_type == "散点图":
            sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
        elif plot_type == "折线图":
            sns.lineplot(data=df, x=x_col, y=y_col, ax=ax)
        elif plot_type == "柱状图":
            sns.barplot(data=df, x=x_col, y=y_col, ax=ax)
        
        ax.set_title(f'{plot_type}: {x_col} vs {y_col}')
        ax.tick_params(axis='x', rotation=45) # 旋转X轴标签, 防止重叠
        plt.tight_layout() # 自动调整布局
        
        # 5. 返回图表对象和更新后的下拉菜单状态
        # Gradio的Plot组件可以直接接收matplotlib的Figure对象.
        return fig, gr.Dropdown.update(choices=columns, value=x_col), gr.Dropdown.update(choices=columns, value=y_col)
        
    except Exception as e:
        # 在出错时返回错误信息
        return str(e), gr.Dropdown.update(choices=[]), gr.Dropdown.update(choices=[])

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 交互式数据分析看板\n上传你的CSV文件, 选择X轴, Y轴和图表类型来动态生成可视化图表.")
    with gr.Row():
        with gr.Column(scale=1): # `scale` 参数可以控制列的相对宽度
            upload_button = gr.UploadButton("上传CSV文件", file_types=[".csv"])
            x_axis_dd = gr.Dropdown(label="选择X轴")
            y_axis_dd = gr.Dropdown(label="选择Y轴")
            plot_type_dd = gr.Dropdown(label="选择图表类型", choices=["散点图", "折线图", "柱状图"], value="散点图")
        with gr.Column(scale=3):
            plot_output = gr.Plot() # Plot组件用于显示matplotlib图表

    # --- 关键的响应式逻辑 ---
    # 定义所有会触发图表更新的输入组件
    inputs = [upload_button, x_axis_dd, y_axis_dd, plot_type_dd]
    # 定义所有需要被更新的输出组件
    outputs = [plot_output, x_axis_dd, y_axis_dd]
    
    # 遍历所有输入组件, 将它们的 `change` 事件都绑定到 `create_plot` 函数上. 
    # 这意味着无论用户是上传了新文件, 还是改变了X/Y轴的选择, 或是更换了图表类型,
    # `create_plot` 都会被自动调用, 从而实现界面的动态更新.
    for component in inputs:
        component.change(fn=create_plot, inputs=inputs, outputs=outputs)

demo.launch()
```

---

## 挑战项目六: API调用与动态内容展示

- **对应模块**: 模块六: AI工具开发者(上) (Web应用基础)
- **项目背景**: 欢迎来到Web的世界! 你每天使用的网站和手机App, 背后都有无数的API (应用程序接口) 在默默工作, 它们就像是数据的“快递员”. 这个项目将带你扮演一个“收件人”的角色, 从一个公共的API服务获取数据, 并将它展示出来. 我们将制作一个非常简单的“每日名言”看板, 点击按钮, 就能从网上获取一句名人名言. 这个过程能让你轻松地理解API的运作方式.

### 核心挑战

1.  **理解API概念**: 从“消费者”的角度, 真正理解API是什么, 以及“请求-响应”的工作模式.
2.  **发送网络请求**: 学会使用Python中最流行的HTTP库`requests`, 向一个真实的API地址发送网络请求.
3.  **解析JSON数据**: 学会处理API返回的`JSON`数据格式, 并从中提取出自己需要的信息.
4.  **动态更新UI**: 将从API获取到的动态内容, 显示在你用`Gradio`制作的用户界面上.

### 技术栈建议

- `requests`: 用于发送HTTP网络请求的Python标准库.
- `Gradio`: 用于快速构建简单的Web用户界面.

### 实现步骤指引

下面的代码展示了如何调用一个免费的“随机名言”API, 并将结果用Gradio展示出来. 在运行前, 请先通过 `pip install requests` 安装`requests`库.

```python
import gradio as gr
import requests # 导入我们用于发送网络请求的库

# --- 1. 核心功能函数: 调用API ---
def get_random_quote():
    """
    调用Quotable API来获取一句随机的名人名言.
    """
    # a. 定义API的URL地址
    api_url = "https://api.quotable.io/random"
    
    try:
        # b. 发送GET请求
        # requests.get() 会向指定的URL发送一个HTTP GET请求, 这就像在浏览器地址栏输入地址后按回车.
        response = requests.get(api_url)
        
        # c. 检查响应状态
        # response.raise_for_status() 是一个好习惯, 如果请求出错(例如网络问题或API服务宕机), 它会抛出异常.
        response.raise_for_status()
        
        # d. 解析JSON数据
        # API返回的数据是JSON格式, .json() 方法可以轻松地将其转换为Python字典.
        data = response.json()
        
        # e. 提取并格式化内容
        # 从字典中获取我们关心的'content'和'author'字段.
        quote = data['content']
        author = data['author']
        
        return f"""__{quote}__"""\n\n— {author}"
        
    except requests.exceptions.RequestException as e:
        # 统一处理所有与网络请求相关的异常
        return f"获取名言失败: 网络错误 ({e})"
    except (KeyError, TypeError) as e:
        # 处理JSON解析或数据提取时可能发生的错误
        return f"获取名言失败: API返回数据格式不正确 ({e})"

# --- 2. 构建Gradio界面 ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 每日名言看板\n点击按钮, 从网络获取一句新的名人名言.")
    
    # 创建一个文本框用于显示名言, lines=5让它有足够的高度.
    quote_output = gr.Textbox(label="名言", lines=5, interactive=False)
    
    # 创建一个按钮
    get_quote_btn = gr.Button("获取一句新的名言", variant="primary")
    
    # --- 3. 设定组件联动 ---
    # 将按钮的 "click" 事件绑定到我们的核心功能函数上.
    # 当用户点击按钮时, `get_random_quote` 函数会被执行, 
    # 并且它的返回值会自动更新到 `quote_output` 文本框中.
    get_quote_btn.click(
        fn=get_random_quote,
        inputs=None, # 我们的函数不需要任何输入
        outputs=quote_output
    )

# --- 4. 启动应用 ---
demo.launch()
```

### 更进一步

当你成功运行这个项目后, 可以尝试指挥你的AI编程助手进行扩展:

*   **增加一个“AI解读”功能**: 添加一个新的按钮, 当用户获取到一句名言后, 点击此按钮可以将名言发送给AI, 让AI来解释这句名言的含义, 并将结果显示在另一个文本框中.
*   **更换API**: 尝试使用我们之前提到的“无聊API”或“狗狗图片API”, 修改代码来适配它们不同的JSON数据结构, 并用合适的Gradio组件(如`Image`组件)来展示结果.

---

## 挑战项目七: 基于RAG的高级问答机器人

- **对应模块**: 模块七 (终极项目实战)
- **项目背景**: Mini版的问答机器人虽然能用, 但它每次都把全部知识发给AI, 既浪费Token又无法处理大文件. 你希望构建一个更高效, 更接近工业应用的问答机器人.

### 核心挑战

亲手实现RAG流程中的**文本分块(Chunking)**, **向量嵌入(Embedding)**和**语义检索(Semantic Search)**.

### 技术栈建议

- `sentence-transformers`, `faiss-cpu`, `numpy`, `Gradio`

### 实现步骤指引

```python
import gradio as gr
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# --- 1. 准备阶段: 构建向量知识库 ---

# a. 加载预训练的句子转换模型. 这个模型能将文本句子转换成高维度的向量.
# 'paraphrase-multilingual-MiniLM-L12-v2' 是一个支持多种语言的轻量级高效模型.
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# b. 定义我们的知识库. 在真实应用中, 这部分内容会从文件或数据库中读取.
KNOWLEDGE_BASE_TEXT = """
第一章: 软件工程简介...
第二章: 编程语言...
第三章: 数据分析...
"""
# c. 文本分块 (Chunking): 将长文本切分成更小的、有意义的块. 这是RAG中的关键一步.
chunks = KNOWLEDGE_BASE_TEXT.strip().split('\n\n')

# d. 向量嵌入 (Embedding): 使用模型将每个文本块转换成一个向量 (一串数字).
# 语义上相似的文本块, 其对应的向量在向量空间中也更接近.
chunk_embeddings = model.encode(chunks)

# e. 构建向量索引 (Indexing): 使用 FAISS (Facebook AI Similarity Search) 来创建一个高效的向量搜索引擎.
# IndexFlatL2 使用L2距离 (欧氏距离) 来计算向量间的相似度.
index = faiss.IndexFlatL2(chunk_embeddings.shape[1])
# 将我们知识库中的所有向量添加到索引中.
index.add(chunk_embeddings)


# --- 2. 核心功能: 检索与生成 ---

def retrieve_and_generate(user_question):
    """
    这个函数实现了RAG的核心流程: 接收用户问题, 检索相关知识, (模拟)生成答案.
    """
    # a. 向量化用户问题: 将用户的问题也转换成和知识库中同维度的向量.
    question_embedding = model.encode([user_question])
    
    # b. 语义检索 (Semantic Search): 在FAISS索引中搜索与问题向量最相似的 k 个向量.
    k = 2 # 我们希望找到最相关的2个知识块.
    # index.search 返回两个值: D (distances, 距离) 和 I (indices, 索引).
    distances, indices = index.search(question_embedding, k)
    
    # c. 提取相关知识: 根据搜索结果的索引, 从原始的 `chunks` 列表中找出最相关的文本块.
    relevant_chunks = [chunks[i] for i in indices[0]]
    context = "\n---\n".join(relevant_chunks)
    
    # d. 构建最终提示 (Prompt Engineering): 将检索到的相关知识 (上下文) 和原始问题组合成一个更丰富的提示.
    # 这是RAG的核心思想: 给大语言模型提供上下文, 让它能基于给定的知识来回答问题, 而不是胡乱猜测.
    final_prompt = f'''请基于以下背景知识:\n\n---\n{context}\n---\n\n来回答这个问题: {user_question}'''
    
    # e. (模拟) 生成答案: 在一个完整的RAG应用中, `final_prompt` 会被发送给一个大型语言模型 (如GPT, Gemini) 来生成最终答案.
    # 这里我们为了简化, 只是模拟了这个过程, 并返回最终的提示和检索到的上下文.
    final_answer = f"(模拟回复) 已找到相关知识...正在根据以上知识回答问题: '{user_question}'"
    
    return final_answer, context

# --- 3. 构建Gradio界面 ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 高级问答机器人 (RAG版)")
    question_input = gr.Textbox(label="你的问题")
    submit_btn = gr.Button("提交")
    answer_output = gr.Textbox(label="AI的回答", lines=5)
    context_output = gr.Textbox(label="检索到的相关知识 (上下文)", lines=5)
    
    submit_btn.click(
        fn=retrieve_and_generate, 
        inputs=question_input, 
        outputs=[answer_output, context_output]
    )

demo.launch()
```

---


