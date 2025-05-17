import json
from sqlalchemy.orm import Session
from ..models.models import Scene, DifficultyLevel

def seed_scenes(db: Session):
    """添加测试场景数据"""
    # 检查是否已有场景数据
    if db.query(Scene).first():
        return
    
    # 咖啡店场景
    coffee_shop = Scene(
        name="咖啡店点餐",
        description="你正在一家美式咖啡店点餐，需要与服务员进行交流。",
        language="英语",
        npc_role="咖啡店服务员",
        npc_description="一位友好的咖啡店服务员，会耐心解答顾客的问题，并提供菜单推荐。",
        difficulty=DifficultyLevel.BEGINNER,
        tasks=json.dumps([
            "向服务员问候并表达想要点餐的意图",
            "询问菜单推荐",
            "选择饮品并说明具体要求（温度、大小等）",
            "选择小点心",
            "确认订单并付款"
        ]),
        tasks_info=json.dumps([
            "咖啡店的菜单有：咖啡、茶、果汁、甜点等",
            "这些菜的特色是：咖啡适合需要提神的人，茶适合需要放松的人，果汁适合需要补充水分和维生素的人，甜点适合需要甜食的人",
            "咖啡可以选择种类：拿铁、卡布奇诺、美式咖啡、摩卡等；可以选择大杯、中杯或者小杯；可以选择冰的或者热的；可以加糖或者不加糖；可以加奶或者不加奶",
            "茶可以选择种类：红茶、绿茶、乌龙茶等；可以选择大杯、中杯或者小杯",
            "果汁可以选择种类：橙汁、苹果汁、西瓜汁等；可以选择大杯、中杯或者小杯",
            "甜点有：蛋糕、饼干、薯条、爆米花等，可以选择大份、中份或者小份",
            "咖啡的价格是：拿铁10元，卡布奇诺12元，美式咖啡10元，摩卡15元；茶的价格是：红茶5元，绿茶5元，乌龙茶8元；果汁的价格是：橙汁8元，苹果汁8元，西瓜汁10元；甜点的价格是：蛋糕10元，饼干8元，薯条10元，爆米花8元"
        ])
    )
    
    # 机场值机场景
    airport = Scene(
        name="机场值机",
        description="你需要在机场办理值机手续，与工作人员进行交流。",
        language="英语",
        npc_role="值机柜台工作人员",
        npc_description="一位专业的机场工作人员，负责帮助旅客办理值机手续。",
        difficulty=DifficultyLevel.INTERMEDIATE,
        tasks=json.dumps([
            "问候并出示护照和机票",
            "回答安全问题",
            "选择座位",
            "询问行李托运事宜",
            "获取登机牌并确认登机时间和登机口"
        ]),
        tasks_info=json.dumps([
            "机场工作人员会用英语回答你的问题",
            
        ])
    )
    
    db.add(coffee_shop)
    db.add(airport)
    db.commit() 