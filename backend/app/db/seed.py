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
        ])
    )
    
    db.add(coffee_shop)
    db.add(airport)
    db.commit() 