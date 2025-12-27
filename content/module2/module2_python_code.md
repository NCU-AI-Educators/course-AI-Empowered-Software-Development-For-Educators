### 第1节课, 第7页 - **最原始的办法：用`print`“写小说”**

```python
# 目标：描述玩家在“扬州广场”的所见所闻
print("你来到了一个叫做“扬州广场”的地方。")
print("你环顾四周，发现这里人来人往，非常热闹。东边是一家茶馆，西边是一家兵器铺。")

# 接着，我们想描述玩家移动到了“茶馆”
print("你来到了一个叫做“茶馆”的地方。")
print("你走了进去，发现里面坐满了茶客，一位说书人正在讲着三国的故事。")
```

### 第1节课, 第9页 - **变量的本质：为“现实世界”创建“数字分身”**

```python
# 为现实世界中的“属性”创建分身
location_description = "..."
player_location = "guangchang"
sword_attack = 10
```

### 第1节课, 第11页 - **变量的威力：数据与逻辑分离**

```python
# 我们为“扬州广场”这个数据，起了个名字叫 location_name
location_name = "扬州广场"

# 描述文本现在也通过拼接变量来生成，而不是写死
location_description = "你正站在" + location_name + "，这里人来人往..."

# 我们可以多次使用这个“名字”
print("欢迎来到 " + location_name)
print(location_description)

# 如果现在需要改名，只需要修改一处！
location_name = "中央广场"
print("地点已更名为: " + location_name)
```

### 第1节课, 第12页 - **变量的动态性：记录玩家移动的“足迹”**

```python
# 玩家的初始位置
player_location = "guangchang"
print(f"你来到了【{player_location}】")

# 玩家决定向东走...
# (在下一课，我们将学习如何根据玩家指令来触发这个改变)
new_location = "chaguan"

# 玩家的位置变化了！“地图标记”被新结果“覆盖”
player_location = new_location
print(f"你移动到了【{player_location}】")
```

### 第1节课, 第15页 - **成功的喜悦与新的挑战**

```python
# 第一个地点
loc1_name = "扬州广场"
loc1_desc = "你正站在扬州城的中央广场..."

# 第二个地点
loc2_name = "茶馆"
loc2_desc = "你走进了一家茶馆，茶香四溢。"

# ... 如果有100个地点？
```

### 第1节课, 第18页 - **架构师的方案：用“字典”为实体建模**

```python
# 用一个“字典”，为“扬州广场”这个实体建模
# “标签”就是属性名，“值”就是属性内容
guangchang = {
    "name": "扬州广场",
    "description": "你正站在扬州城的中央广场...",
    "exits": {"east": "chaguan"}
}

# 现在，一个变量就代表一个完整的实体！
# 我们可以清晰地获取它的任何属性
print(guangchang["description"])
```

### 第1节课, 第20页 - **世界蓝图：玩家与数据类型**

```python
player = {
    "name": "令狐冲",
    "level": 1,
    "health": 100,
    "inventory": ["新手布衣", "一把生锈的剑"],
    "current_location": "guangchang"
}
```

### 第1节课, 第21页 - **类型为何重要？`100 + 50` 与 `"100" + "50"`**

```python
# 玩家喝了一瓶治疗药水
player_health = 100
potion_effect = 50

# 结果是 150 (玩家成功回血)
player_health = player_health + potion_effect
```

### 第1节课, 第21页 - **类型为何重要？`100 + 50` 与 `"100" + "50"`**

```python
# 系统想显示玩家的等级
level_text = "等级: "
player_level = "1" # 注意，这里的1是文本

# 结果是 "等级: 1"
level_display = level_text + player_level
```

### 第2节课, 第7页 - **核心概念1：布尔值——只有“真”或“假”的世界**

```python
# 我们可以直接打印出一个“判断题”的答案
command = "/quit"

print("指令是不是'/quit'?", command == "/quit")

print("指令是不是'/look'?", command == "/look")

print("玩家等级是不是大于10?", 15 > 10)
```

### 第2节课, 第9页 - **核心语法1：用 `If-Else` 搭建第一个“T字路口”**

```python
command = "/go east"

# 计算机算出 command == "/quit" 是 False (开关是关的)
if command == "/quit": 
    # 因为开关是关的，所以这部分代码被跳过
    print("你退出了江湖...")
else: 
    # 程序走到这里，执行这个代码块
    print("游戏继续...")
```

### 第2节课, 第9页 - **核心语法1：用 `If-Else` 搭建第一个“T字路口”**

```python
  if <条件表达式>:
      # 条件为 True 时执行的代码块
      # 这个代码块必须缩进
      ...
  else:
      # 条件为 False 时执行的代码块
      # 这个代码块也必须缩进
      ...
```

### 第2节课, 第10页 - **核心语法2：用 `elif` 搭建“立交桥”**

```python
command = "/look"

if command == "/go": # 第1个判断
    print("处理移动逻辑...")
elif command == "/look": # 如果第1个判断为假，则进行第2个判断
    print("处理观察逻辑...")
elif command == "/get": # 如果前2个判断都为假，则进行第3个判断
    print("处理拾取逻辑...")
else: # 如果以上所有判断都为假
    print("无效的指令！")
```

### 第2节课, 第10页 - **核心语法2：用 `elif` 搭建“立交桥”**

```python
  if <条件1>:
      # 条件1为True时执行
  elif <条件2>:
      # 条件1为False，但条件2为True时执行
  elif <条件3>:
      # 条件1和2都为False，但条件3为True时执行
  ...
  else:
      # 以上所有条件都为False时执行
```

### 第2节课, 第14页 - **AI的实现与我们的关注点**

```python
# ... (之前的世界定义代码) ...

# 根据 player_location 变量的值，从 world 字典中获取玩家所在地的描述，并打印出来
print("\n=== 武侠世界 ===")
print(world[player_location]['description'])

# 获取玩家输入
command = input("\n请输入指令（输入/quit退出）：")

# 判断玩家输入
if command == "/quit":
    print("你退出了江湖...")  
```

### 第2节课, 第15页 - **第二步：实现完整的指令解析**

```python
  elif command.startswith("/go "):
      # 外层判断为True后，进入这个代码块
      direction = ...
      if direction in exits: # 内层判断
          # ...
      else:
          # ...
```

### 第2节课, 第16页 - **AI的最终代码与审查**

```python
# ... (前面是没有变化的代码) ...
# 判断玩家输入
if command == "/quit":
    print("你退出了江湖...")
elif command == "/look":
    # 重新打印当前地点的描述
    print(world[player_location]['description'])
elif command.startswith("/go "):
    # 解析方向参数
    direction = command.split(" ", 1)[1]  # 获取/go后面的部分，例如"east"
    
    # 检查这个方向是否是当前地点的一个有效出口
    if direction in world[player_location]['exits']:
        # 更新 player_location 变量为新的地点ID
        new_location = world[player_location]['exits'][direction]
        player_location = new_location
        
        # 打印提示
        print(f"你来到了{new_location}...")
    else:
        # 不是有效出口，打印错误信息
        print("你不能往那个方向走。")
else:
    # 对于所有其他无法识别的指令，打印无效指令提示
    print("无效的指令！")

```

### 第3节课, 第7页 - **升级蓝图：用`列表(List)`丰富世界**

```python
world = {
    'guangchang': {
        'description': '这里是扬州广场，人来人往。',
        'exits': {'east': 'chaguan'},
        'items': ['一柄生锈的铁剑', '一个啃过的苹果'] # 新增！
    },
    'chaguan': {
        # ...
    }
}
```

### 第3节课, 第8页 - **`for`循环：自动化流水线**

```python
# 1. 准备“传送带”上的“原料”
items_in_room = ['一柄生锈的铁剑', '一个啃过的苹果']

# 2. 搭建流水线，告诉它去处理 items_in_room 这个列表
for item in items_in_room:

    # 3. 设计“机械臂”的动作 (所有缩进的代码)
    #    对每一个传送过来的 item，都执行一次打印
    print(f"你发现地上有: {item}")
```

### 第3节课, 第9页 - **架构师笔记：Python的“缩进”美学**

```python
# 这行代码在循环“外面”
print("循环即将开始...")

for item in a_list:
    # 这行代码在循环“里面”
    # 它属于 for 循环“管辖”
    print(f"处理: {item}")

# 这行代码也在循环“外面”
print("循环已结束。")
```

### 第3节课, 第10页 - **`while`循环：游戏世界的“心跳”**

```python
while True:
    # 只要宇宙不毁灭 (True永远是True)
    # 就永远、不知疲倦地
    # 重复执行这里的所有代码
    
    print("游戏世界的心跳...咚...")
    # (为了避免无限打印刷屏，我们让它暂停一下)
    import time
    time.sleep(1)
```

### 第3节课, 第11页 - **`break`：紧急制动，跳出循环**

```python
while True:
    command = input("请输入指令 (输入/quit退出): ")
    
    if command == "/quit":
        print("你决定退出江湖...")
        break # 条件满足，执行“紧急制动”，跳出while循环
    
    print(f"你输入了: {command}")

# break后，程序会跳转到这里继续执行
print("游戏已结束。")
```

### 第3节课, 第12页 - **思考题：另一种“熄火”方式**

```python
# 1. 设置一个“开关”变量，初始状态为“开”
game_is_running = True

# 2. 循环的持续，依赖于这个“开关”的状态
while game_is_running:
    command = input("> ")
    if command == "/quit":
        # 3. 当满足退出条件时，我们只需关掉“开关”
        print("你决定退出江湖...")
        game_is_running = False

# 4. 开关关闭后，循环在下一次检查条件时，就会自然结束
print("游戏已结束。")
```

### 第3节课, 第13页 - **方案对比：“状态变量” vs `break`**

```python
game_is_running = True
while game_is_running:
    command = input("> ")
    if command == "/quit":
        game_is_running = False

print("游戏已结束。")
```

### 第3节课, 第13页 - **方案对比：“状态变量” vs `break`**

```python
while True:
    command = input("> ")
    if command == "/quit":
        break 

print("游戏已结束。")
```

### 第3节课, 第17页 - **敏锐的观察：为何/look会重复描述？**

```python
# 游戏主循环
while True:
    # 1. 无条件打印当前地点描述
    print(world[player_location]['description'])

    # 2. 获取并处理指令
    command = input("> ")
    if command == "/look":
        # 3. /look指令又打印了一次描述
        print(world[player_location]['description'])
    # ... 其他指令
```

### 第4节课, 第12页 - **新的“痛点”：臃肿的主循环**

```python
while True:
    # ...
    if command.startswith("/go "):
        # 处理go的一大段代码
    elif command.startswith("/take "):
        # 处理take的一大段代码
    elif command.startswith("/drop "):
        # 处理drop的一大段代码
    elif command.startswith("/talk "):
        # 处理talk的一大段代码
    # ... 更多更多的elif
```

