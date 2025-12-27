# -*- coding: utf-8 -*- 

# =============================================================================
# 《AI赋能软件开发》课程
# 模块三，第10课 起始代码 (v1.2 - 史诗级更新)
#
# 本文件是第9课函数重构练习之后的结果。
# 原本臃肿的主循环已经被拆分成多个独立的函数，代码结构更加清晰。
# 主循环现在扮演着“指挥中心”的角色，负责分发任务。
#
# v1.2更新:
# - 扩展了游戏世界，增加了铁匠铺、药铺等多个地点。
# - 增加了NPC系统，并添加了相关的/talk和/ask指令。
# - 增加了一个创新的“上帝视角”指令 /godmode，用于随机执行指令序列。
#   (注意/godmode的实现方式与v2版本有何不同，体会函数复用的威力)
# =============================================================================
import random
import time

# --- 游戏数据定义 ---

# 游戏世界
world = {
    'guangchang': {
        'name': '扬州广场',
        'description': '你现在位于扬州城的中心广场，人来人往，热闹非凡。四周的建筑鳞次栉比。\n往南是一家客栈，往北是一家茶馆，往西是铁匠铺，往东是药铺。',
        'exits': {'south': 'kezhan', 'north': 'chaguan', 'west': 'tjiangpu', 'east': 'yaopu'},
        'items': ['布告栏']
    },
    'kezhan': {
        'name': '客栈',
        'description': '这是一家寻常的客栈，掌柜的正在柜台后打着算盘。空气中弥漫着饭菜和酒的香气。',
        'exits': {'north': 'guangchang'},
        'items': ['店小二', '空桌子']
    },
    'chaguan': {
        'name': '茶馆',
        'description': '茶馆里坐着几桌客人，一位说书先生正在滔滔不绝地讲述着江湖轶事。',
        'exits': {'south': 'guangchang'},
        'items': []
    },
    'tjiangpu': {
        'name': '铁匠铺',
        'description': '这里是城西的铁匠铺，炉火正旺，一个健壮的铁匠正在满头大汗地打铁。',
        'exits': {'east': 'guangchang'},
        'items': ['铁锤', '火炉']
    },
    'yaopu': {
        'name': '药铺',
        'description': '药铺里弥漫着浓郁的药材味，一个老药师正在整理药柜。',
        'exits': {'west': 'guangchang'},
        'items': ['金疮药', '药柜']
    }
}

# NPC定义
npcs = {
    'shushuxiansheng': {
        'name': '说书先生',
        'location': 'chaguan',
        'dialogue': {
            'default': '说书先生呷了一口茶，说道：“话说天下大势，分久必合，合久必分……”',
            '扬州': '“扬州城自古繁华，乃交通要道，藏龙卧虎之辈不计其数。”',
            '宝剑': '“要说宝剑，那还得是城西铁匠铺的张师傅，他祖上可是干将莫邪的传人！”'
        }
    },
    'laoyashi': {
        'name': '老药师',
        'location': 'yaopu',
        'dialogue': {
            'default': '老药师抬眼看了看你：“客官，要抓药还是看病？”',
            '金疮药': '“我这的金疮药可是祖传秘方，对刀剑伤有奇效。”',
            '健康': '“年轻人，身体才是根本啊。平时要多加锻炼，固本培元。”'
        }
    },
    'tiejiang': {
        'name': '铁匠',
        'location': 'tjiangpu',
        'dialogue': {
            'default': '铁匠擦了擦汗，瓮声瓮气地问：“要打造点什么？”',
            '宝剑': '“寻常刀剑我这都有，但若想打造神兵利器，非得有天外玄铁不可。”',
            '玄铁': '“玄铁乃天外陨石所化，坚硬无比，世间罕见。若能得之，我愿为你免费铸剑！”'
        }
    }
}

# 表情库
emotes = [
    "你负手而立，眼神深邃，一股宗师气度油然而生。",
    "你仰天长笑，声震四野，惊起林中飞鸟无数。",
    "你眉头紧锁，似乎在思索着什么武学上的难题。",
    "你对月独酌，一杯敬过往，一杯敬远方。",
    "你席地而坐，抚弄着身前的古琴，琴音袅袅，引人入胜。",
    "你嘴角微微上扬，露出一丝神秘的微笑。"
]

# 招式库
skills = [
    "你深吸一口气，猛然打出一招【降龙十八掌之亢龙有悔】，掌风呼啸，气势磅礴！",
    "你身形飘忽，使出【凌波微步】，众人只觉眼前一花，你已在数丈之外。",
    "你剑指苍天，引来一道惊雷，正是【神剑御雷真诀】，煌煌天威，不可直视！",
    "你口中念念有词，手中结印，一朵冰莲在掌心绽放，寒气逼人，此乃【冰心诀】。",
    "你双掌画圆，一个太极图浮现身前，将所有攻击化为无形，正是【太极拳之揽雀尾】。",
    "你拔剑出鞘，剑光如水，一式【独孤九剑之破剑式】，直指对方破绽！"
]


# --- 核心功能函数 ---

def handle_look(current_room_data, npcs_data, player_location):
    """处理观察指令，打印房间信息、物品和NPC。"""
    print(current_room_data['name'])
    print(current_room_data['description'])
    if current_room_data['items']:
        print("你看到了: " + ", ".join(current_room_data['items']))
    else:
        print("这里似乎没什么特别的东西。")
    
    npc_found = False
    for npc_id, npc_data in npcs_data.items():
        if npc_data['location'] == player_location:
            print(f"{npc_data['name']}也在这里。")
            npc_found = True
            break
    if not npc_found:
        print("这里除了你没有别人了。")

def handle_go(argument, current_room_data, current_location):
    """处理移动指令，返回新的玩家位置。"""
    if not argument:
        print("请指定方向, 如: /go south")
        return current_location
        
    direction = argument
    if direction in current_room_data['exits']:
        return current_room_data['exits'][direction]
    else:
        print(f"你无法向 {direction} 方向移动。")
        return current_location

def handle_take(argument, current_room_data, inventory):
    """处理拾取指令。"""
    if not argument:
        print("请指定要拾取的物品, 如: /take 布告栏")
        return
    if argument in current_room_data['items']:
        current_room_data['items'].remove(argument)
        inventory.append(argument)
        print(f"你拾取了 {argument}。")
    else:
        print(f"这里没有 {argument}。")

def handle_drop(argument, current_room_data, inventory):
    """处理丢弃指令。"""
    if not argument:
        print("请指定要丢弃的物品, 如: /drop 布告栏")
        return
    if argument in inventory:
        inventory.remove(argument)
        current_room_data['items'].append(argument)
        print(f"你丢下了 {argument}。")
    else:
        print(f"你的行囊里没有 {argument}。")

def handle_inventory(inventory):
    """处理背包指令。"""
    if inventory:
        print("你的物品: " + ", ".join(inventory))
    else:
        print("你的行囊空空如也。")

def handle_talk(argument, npcs_data, player_location):
    """处理交谈指令。"""
    if not argument:
        print("你想和谁交谈? /talk [NPC名字]")
        return
    
    npc_found = False
    for npc_id, npc_data in npcs_data.items():
        if npc_data['location'] == player_location and npc_data['name'].lower() == argument:
            print(npc_data['dialogue']['default'])
            npc_found = True
            break
    if not npc_found:
        print(f"这里没有叫 {argument} 的人。")

def handle_ask(argument, npcs_data, player_location):
    """处理询问指令。"""
    if 'about' not in argument:
        print("指令格式错误。请使用: /ask [NPC名字] about [话题]")
        return
    
    parts = argument.split('about')
    target_npc_name = parts[0].strip()
    topic = parts[1].strip()

    npc_found = False
    for npc_id, npc_data in npcs_data.items():
        if npc_data['location'] == player_location and npc_data['name'].lower() == target_npc_name:
            npc_found = True
            if topic in npc_data['dialogue']:
                print(f"你向{npc_data['name']}打听关于“{topic}”的事：")
                print(npc_data['dialogue'][topic])
            else:
                print(f"{npc_data['name']}想了想，说：“这个……我也不太清楚。”")
            break
    if not npc_found:
        print(f"这里没有叫 {target_npc_name} 的人。")

def handle_emote(argument, emotes_list):
    """处理表情指令。"""
    if argument:
        print(f"你{argument}。")
    else:
        print(random.choice(emotes_list))

def handle_cast(argument, skills_list):
    """处理招式指令。"""
    if argument:
        print(f"你使出了一招【{argument}】，看起来平平无奇。")
    else:
        print(random.choice(skills_list))

def generate_godmode_sequence():
    """生成一个随机的指令序列用于上帝模式。"""
    possible_commands = [
        '/look', '/go north', '/go south', '/go west', '/go east',
        '/talk 说书先生', '/ask 说书先生 about 扬州', '/talk 铁匠', '/ask 铁匠 about 玄铁',
        '/take 铁锤', '/drop 铁锤', '/inventory', '/emote', '/cast'
    ]
    return random.choices(possible_commands, k=5)

# --- 游戏主程序 ---

def main():
    """游戏的主函数，包含主循环。"""
    player_location = 'guangchang'
    inventory = []

    print("--- 欢迎来到武侠世界 ---")
    print("你可以使用的指令: /go, /look, /take, /drop, /inventory, /talk, /ask, /emote, /cast, /godmode, /quit")
    print("==========================================")

    handle_look(world[player_location], npcs, player_location)

    while True:
        print("-" * 20)
        command_input = input("> ").lower().strip()
        
        if command_input == '/godmode':
            print("--- 上帝模式开启，命运的齿轮开始转动... ---")
            command_sequence = generate_godmode_sequence()
            for cmd in command_sequence:
                time.sleep(1.5)
                print(f"\n[上帝模式]: 自动执行 -> {cmd}")
                # 复用指令处理逻辑
                player_location, inventory = process_command(cmd, player_location, inventory)
            print("\n--- 上帝模式结束 ---")
            continue

        player_location, inventory = process_command(command_input, player_location, inventory)
        if player_location is None: # 退出信号
            break

def process_command(command_input, player_location, inventory):
    """处理单个指令，并返回更新后的玩家状态。"""
    if not command_input:
        return player_location, inventory
        
    parts = command_input.split(' ')
    command = parts[0]
    argument = " ".join(parts[1:])
    
    current_room_data = world[player_location]

    if command == '/quit':
        print("感谢游玩，再见！")
        return None, None # 返回None作为退出信号

    elif command == '/look':
        handle_look(current_room_data, npcs, player_location)
    elif command == '/go':
        new_location = handle_go(argument, current_room_data, player_location)
        if new_location != player_location:
            player_location = new_location
            print(f"你移动到了 {world[player_location]['name']}。")
            handle_look(world[player_location], npcs, player_location)
    elif command == '/take':
        handle_take(argument, current_room_data, inventory)
    elif command == '/drop':
        handle_drop(argument, current_room_data, inventory)
    elif command == '/inventory':
        handle_inventory(inventory)
    elif command == '/talk':
        handle_talk(argument, npcs, player_location)
    elif command == '/ask':
        handle_ask(argument, npcs, player_location)
    elif command == '/emote':
        handle_emote(argument, emotes)
    elif command == '/cast':
        handle_cast(argument, skills)
    else:
        print("无效指令。")
        
    return player_location, inventory

# --- 脚本入口 ---
if __name__ == "__main__":
    main()
