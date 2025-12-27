from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, Response
from pydantic import BaseModel
from typing import List, Optional, Deque, Dict
from collections import deque
import socket
import qrcode
import io
import pathlib
import random

app = FastAPI()

# --- Configuration: CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Data Structures (In-Memory Database) ---

# 1. World Map (Static Graph)
world = {
    "广场": {
        "desc": "这里是桃花岛的中心广场，阳光明媚，微风拂面。",
        "exits": {"north": "客栈", "east": "码头", "west": "铁匠铺", "south": "试剑亭"},
        "npc": [],
        "items": []
    },
    "客栈": {
        "desc": "一家古色古香的客栈，名为'悦来客栈'。店小二正在擦桌子。",
        "exits": {"south": "广场", "east": "厨房"},
        "npc": ["店小二"],
        "items": ["陈年女儿红"]
    },
    "厨房": {
        "desc": "这里烟熏火燎，香气扑鼻，灶台上正炖着一只叫花鸡。",
        "exits": {"west": "客栈"},
        "npc": ["黄蓉"],
        "items": ["叫花鸡", "好逑汤"]
    },
    "码头": {
        "desc": "通往中原的码头，海浪拍打着岸边，几只海鸥在飞翔。",
        "exits": {"west": "广场"},
        "npc": [],
        "items": ["小渔船"]
    },
    "铁匠铺": {
        "desc": "叮叮当当！打铁声不绝于耳，这里热浪滚滚。",
        "exits": {"east": "广场"},
        "npc": ["冯默风"],
        "items": ["大铁锤"]
    },
    "试剑亭": {
        "desc": "一处位于峭壁之上的凉亭，四周云雾缭绕，是习武切磋的好地方。",
        "exits": {"north": "广场", "east": "藏经阁"},
        "npc": ["郭靖"],
        "items": []
    },
    "藏经阁": {
        "desc": "书架上摆满了武功秘籍，空气中弥漫着书香。",
        "exits": {"west": "试剑亭"},
        "npc": ["周伯通"],
        "items": ["九阴真经", "左右互搏术"]
    }
}

# NPC Dialogues
npc_dialogues = {
    "店小二": ["客官，打尖还是住店？", "新到了上好的女儿红，要不尝尝？"],
    "黄蓉": ["靖哥哥去哪了？", "这只叫花鸡火候刚好，快尝尝！", "爹爹又关禁闭了..."],
    "郭靖": ["侠之大者，为国为民。", "蓉儿，你做的菜真好吃。", "降龙十八掌，第一式！"],
    "冯默风": ["打铁也是一种修行。", "这块玄铁可是宝贝。"],
    "周伯通": ["好玩好玩！快来陪我打架！", "我左手画方，右手画圆，你学会了吗？"],
}

# 2. Player Session (Dynamic State)
players = {}

# 3. Global Chat Log (Last 20 messages)
chat_log: Deque[str] = deque(maxlen=20)

# --- Models ---
class PlayerAction(BaseModel):
    uid: str
    target: Optional[str] = None 

# --- Helpers ---
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def trigger_npc_event(room_name: str):
    """Event-driven NPC logic"""
    room_info = world.get(room_name)
    if not room_info: return

    npcs = room_info.get("npc", [])
    if npcs: # Always trigger if NPC is present
        npc = random.choice(npcs)
        lines = npc_dialogues.get(npc, ["..."])
        msg = f"🤖 {npc}: {random.choice(lines)}"
        chat_log.append(msg)

# --- Endpoints ---

@app.get("/", response_class=HTMLResponse)
def serve_home():
    return pathlib.Path("index.html").read_text(encoding="utf-8")

@app.get("/qrcode")
def get_qr_image():
    """Generate QR Code for the server URL"""
    ip = get_local_ip()
    url = f"http://{ip}:8000"
    
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return Response(content=buf.getvalue(), media_type="image/png")

@app.post("/login")
def login(action: PlayerAction):
    if action.uid not in players:
        players[action.uid] = {"loc": "广场"}
        chat_log.append(f"📢 系统: 欢迎少侠 {action.uid} 踏入江湖！")
        trigger_npc_event("广场") # Trigger NPC
        return {"code": 200, "message": f"Welcome, {action.uid}!"}
    else:
        return {"code": 200, "message": f"Welcome back, {action.uid}!"}

@app.get("/state")
def get_state(uid: str, last_idx: int = 0):
    if uid not in players:
        raise HTTPException(status_code=404, detail="Player not found")
    
    current_room_name = players[uid]["loc"]
    room_info = world[current_room_name]
    
    # 1. Get Players
    others = [
        name for name, data in players.items() 
        if data["loc"] == current_room_name and name != uid
    ]
    
    # 2. Get NPCs (Static info only)
    current_npcs = room_info.get("npc", [])

    return {
        "code": 200,
        "data": {
            "room": current_room_name,
            "desc": room_info["desc"],
            "exits": list(room_info["exits"].keys()),
            "items": room_info.get("items", []),
            "npcs": current_npcs,
            "others": others,
            "chat": list(chat_log)
        }
    }

@app.post("/move")
def move(action: PlayerAction):
    if action.uid not in players:
        raise HTTPException(status_code=404, detail="Player not found")
    
    current_room_name = players[action.uid]["loc"]
    room_exits = world[current_room_name]["exits"]
    direction = action.target
    
    if direction in room_exits:
        new_room = room_exits[direction]
        players[action.uid]["loc"] = new_room
        trigger_npc_event(new_room) # Trigger NPC
        return {"code": 200, "message": f"你前往了 {new_room}"}
    else:
        return {"code": 400, "message": "那边没有路！"}

@app.post("/shout")
def shout(action: PlayerAction):
    """Global Chat"""
    if action.uid not in players:
        raise HTTPException(status_code=404, detail="Player not found")
    
    msg = action.target
    if msg:
        chat_log.append(f"[{action.uid}]: {msg}")
        return {"code": 200, "message": "Sent"}
    return {"code": 400, "message": "Empty message"}

if __name__ == "__main__":
    import uvicorn
    # Print logic kept for terminal users
    ip = get_local_ip()
    print(f"\n🚀 Server running at: http://{ip}:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
