# -*- coding: utf-8 -*-

# =============================================================================
# 《AI赋能软件开发》课程
# 模块三，第9课 起始代码 (v1.2 - 史诗级更新)
#
# 本文件代表模块二结束时，一个功能完整但结构臃肿的武侠MUD游戏。
# 所有的游戏逻辑都堆积在主`while`循环中，导致代码难以阅读和维护。
# 这是我们将在第9课中进行“函数重构”的完美起点。
#
# v1.2更新:
# - 扩展了游戏世界，增加了铁匠铺、药铺等多个地点。
# - 增加了NPC系统，并添加了相关的/talk和/ask指令。
# - 增加了一个创新的“上帝视角”指令 /godmode，用于随机执行指令序列。
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


# --- 游戏初始化 ---

player_location = 'guangchang'
inventory = []

print("--- 欢迎来到武侠世界 ---")
print("你可以使用的指令: /go, /look, /take, /drop, /inventory, /talk, /ask, /emote, /cast, /godmode, /quit")
print("==========================================")

# 初始时显示一次房间信息
print(world[player_location]['name'])
print(world[player_location]['description'])
if world[player_location]['items']:
    print("你看到了: " + ", ".join(world[player_location]['items']))
# 显示NPC
for npc_id, npc_data in npcs.items():
    if npc_data['location'] == player_location:
        print(f"{npc_data['name']}也在这里。")


# --- 游戏主循环 ---

while True:
    print("-" * 20)
    command_input = input("> ").lower().strip()
    
    if not command_input:
        continue
        
    parts = command_input.split(' ')
    command = parts[0]
    argument = " ".join(parts[1:])

    if command == '/quit':
        print("感谢游玩，再见！")
        break

    elif command == '/look':
        current_room = world[player_location]
        print(current_room['name'])
        print(current_room['description'])
        if current_room['items']:
            print("你看到了: " + ", ".join(current_room['items']))
        else:
            print("这里似乎没什么特别的东西。")
        # 显示NPC
        npc_found = False
        for npc_id, npc_data in npcs.items():
            if npc_data['location'] == player_location:
                print(f"{npc_data['name']}也在这里。")
                npc_found = True
        if not npc_found:
            print("这里除了你没有别人了。")


    elif command == '/go':
        if not argument:
            print("请指定方向, 如: /go south")
            continue
            
        direction = argument
        current_room = world[player_location]
        
        if direction in current_room['exits']:
            new_location = current_room['exits'][direction]
            player_location = new_location
            # 移动后自动执行look
            new_room = world[player_location]
            print(f"你移动到了 {new_room['name']}。")
            print(new_room['description'])
            if new_room['items']:
                print("你看到了: " + ", ".join(new_room['items']))
            # 显示NPC
            for npc_id, npc_data in npcs.items():
                if npc_data['location'] == player_location:
                    print(f"{npc_data['name']}也在这里。")
        else:
            print(f"你无法向 {direction} 方向移动。")

    elif command == '/take':
        if not argument:
            print("请指定要拾取的物品, 如: /take 布告栏")
            continue
            
        item_to_take = argument
        current_room = world[player_location]

        if item_to_take in current_room['items']:
            current_room['items'].remove(item_to_take)
            inventory.append(item_to_take)
            print(f"你拾取了 {item_to_take}。")
        else:
            print(f"这里没有 {item_to_take}。")
            
    elif command == '/drop':
        if not argument:
            print("请指定要丢弃的物品, 如: /drop 布告栏")
            continue
            
        item_to_drop = argument
        if item_to_drop in inventory:
            inventory.remove(item_to_drop)
            world[player_location]['items'].append(item_to_drop)
            print(f"你丢下了 {item_to_drop}。")
        else:
            print(f"你的行囊里没有 {item_to_drop}。")
            
    elif command == '/inventory':
        if inventory:
            print("你的物品: " + ", ".join(inventory))
        else:
            print("你的行囊空空如也。")
            
    elif command == '/talk':
        if not argument:
            print("你想和谁交谈? /talk [NPC名字]")
            continue
        
        target_npc_name = argument
        npc_found = False
        for npc_id, npc_data in npcs.items():
            if npc_data['location'] == player_location and npc_data['name'].lower() == target_npc_name:
                print(npc_data['dialogue']['default'])
                npc_found = True
                break
        if not npc_found:
            print(f"这里没有叫 {target_npc_name} 的人。")

    elif command == '/ask':
        # /ask [npc] about [topic]
        if 'about' not in argument:
            print("指令格式错误。请使用: /ask [NPC名字] about [话题]")
            continue
        
        parts = argument.split('about')
        target_npc_name = parts[0].strip()
        topic = parts[1].strip()

        npc_found = False
        for npc_id, npc_data in npcs.items():
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

    elif command == '/emote':
        if argument:
            print(f"你{argument}。")
        else:
            print(random.choice(emotes))
            
    elif command == '/cast':
        if argument:
            print(f"你使出了一招【{argument}】，看起来平平无奇。")
        else:
            print(random.choice(skills))
            
    elif command == '/godmode':
        print("--- 上帝模式开启，命运的齿轮开始转动... ---")
        possible_commands = [
            '/look', '/go north', '/go south', '/go west', '/go east',
            '/talk 说书先生', '/ask 说书先生 about 扬州', '/talk 铁匠', '/ask 铁匠 about 玄铁',
            '/take 铁锤', '/drop 铁锤', '/inventory', '/emote', '/cast'
        ]
        command_sequence = random.choices(possible_commands, k=5)
        
        for cmd in command_sequence:
            time.sleep(1.5)
            print(f"\n[上帝模式]: 自动执行 -> {cmd}")
            
            # --- 这里是完全重复的、臃肿的代码逻辑，完美地展示了“坏代码”的危害 ---
            god_parts = cmd.split(' ')
            god_command = god_parts[0]
            god_argument = " ".join(god_parts[1:])

            if god_command == '/look':
                # ... (此处省略与上方/look完全重复的数百行代码)
                print("执行 /look...")
            elif god_command == '/go':
                # ... (此处省略与上方/go完全重复的数百行代码)
                print(f"执行 /go {god_argument}...")
            # ... 对每一个可能在godmode中出现的指令，都需要把上面的逻辑复制一遍
            # ... 为了幻灯片演示的简洁，我们仅打印文字，但在真实场景中，这将导致代码极度冗余
            print(f"(正在模拟执行 {god_command} 指令...)")
        print("\n--- 上帝模式结束 ---")


    else:
        print("无效指令。")
