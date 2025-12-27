### 第9节课 - **回顾：新的“痛点”——臃肿的主循环**

```python
while True:
    # ...
    if command.startswith("/go "):
        # 处理go的一大段代码
    elif command.startswith("/take "):
        # 处理take的一大段代码
    # ... 更多更多的elif
```

### 第9节课 - **核心比喻：从“菜谱”到“微波炉”**

```python
# 第一次加热
print("拿出盘子")
print("放入剩菜")
print("设置1分钟")
print("开始加热")

# 第二次加热
print("拿出盘子")
print("放入牛奶")
print("设置30秒")
print("开始加热")
```

```python
def heat_food(food, time):
    print("拿出盘子")
    print(f"放入{food}")
    print(f"设置{time}")
    print("开始加热")

# 调用函数
heat_food("剩菜", "1分钟")
heat_food("牛奶", "30秒")
```

### 第9节课 - **函数的“解剖学”：定义与调用**

```python
# def 关键字，表示“我要定义一个函数”
# handle_look 是我们为这个功能起的名字
# () 里是“参数列表”，是它工作需要的“原料”
def handle_look(world, player_location):
    
    # 缩进的代码块，是这个函数的“功能主体”
    print("--- 观察四周 ---")
    print(world[player_location]['description'])
    # ... (更多处理逻辑)
```

```python
# 在主循环中
# ...
elif command == "/look":
    # 调用我们定义的函数
    # 并把当前的世界地图和玩家位置作为“原料”传给它
    handle_look(world, player_location)
```

### 第9节课 - **重构第一步：将`/look`指令封装成函数**

```python
# 主循环
while True:
    # ...
    elif command == "/look":
        # 所有细节都堆在这里
        print(world[player_location]['description'])
        if 'items' in world[player_location]:
            for item in world[player_location]['items']:
                print(f"你看到了: {item}")
        # ... 更多代码
```

```python
# 1. 在主循环外部，定义函数
def show_room_details(world, player_location):
    print(world[player_location]['description'])
    if 'items' in world[player_location]:
        for item in world[player_location]['items']:
            print(f"你看到了: {item}")
    # ... 更多代码

# 2. 在主循环内部，调用函数
while True:
    # ...
    elif command == "/look":
        show_room_details(world, player_location)
```

### 第9节课 - **重构的价值：清晰的“指挥中心”**

```python
# 重构后的主循环
while True:
    command = input("> ")

    if command == "/quit":
        handle_quit() # 调用“处理退出”的函数
    
    elif command.startswith("/go"):
        handle_go(command, world, player_location) # 调用“处理移动”的函数

    elif command.startswith("/take"):
        handle_take(command, world, player_location) # 调用“处理拾取”的函数

    elif command == "/look":
        handle_look(world, player_location) # 调用“处理观察”的函数
        
    else:
        handle_unknown_command() # 调用“处理未知指令”的函数
```

### 第9节课 - **迭代指令：用`return`重构`handle_go`**

```python
# handle_go 函数内部
def handle_go(command, world, current_loc):
    # ... (一堆处理逻辑)
    
    if direction_is_valid:
        new_loc = ... # 计算出新的地点
        print("你移动到了...")
        return new_loc # 将新地点作为“结果”返回
    else:
        print("无法移动...")
        return current_loc # 移动失败，将旧地点原样返回

# 主循环中
while True:
    # ...
    elif command.startswith("/go"):
        # “接收”函数返回的结果，并用它更新主循环中的状态
        player_location = handle_go(...)
```

### 第10节课 - **案发现场：Python的“事故报告” (Traceback)**

```
Traceback (most recent call last):
  File "C:/Users/Hawk/game.py", line 52, in <module>
    player_location = handle_go(command, world, player_location)
  File "C:/Users/Hawk/game.py", line 28, in handle_go
    new_location_data = world[new_location_id]
KeyError: 'market'
```

### 第10节课 - **动手环节(1/3)：布置“案发现场”**

```python
'guangchang': {
    'description': '这里是扬州广场...',
    # 将'chaguan'改成一个不存在的'market'
    'exits': {'east': 'market'}, 
    'items': [...]
},
# (我们的world里并没有'market'这个地点)
```

### 第11节课 - **动手场景：优化`/look`指令的“出口”显示**

```python
def show_exits(world, player_location):
    exits = world[player_location].get('exits', {})
    if not exits:
        return # 如果没有出口，直接返回
        
    exits_string = "此地出口: "
    for direction, destination in exits.items():
        # 手动拼接字符串和空格
        exits_string += f"{direction}({destination}) "
        
    print(exits_string)
```

### 第11节课 - **动手环节(2/2)：要求AI“对比分析”**

```python
def show_exits_pythonic(world, player_location):
    exits = world[player_location].get('exits', {})
    if not exits:
        return
        
    # 使用列表推导式和join方法
    exit_parts = [f"{direction}({destination})" for direction, destination in exits.items()]
    exits_string = "此地出口: " + ", ".join(exit_parts)
    
    print(exits_string)
```

```python
exit_parts = []
for direction, destination in exits.items():
    part = f"{direction}({destination})"
    exit_parts.append(part)
```
