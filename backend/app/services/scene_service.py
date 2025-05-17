from typing import List, Dict
from ..models.scene import Scene

# 示例场景数据
SCENES: Dict[str, Scene] = {
    "coffee_shop": Scene(
        id="coffee_shop",
        title="咖啡店点餐",
        description="在咖啡店与服务员进行点餐对话",
        difficulty="beginner",
        estimated_time=15,
        tasks=[
            "向服务员问候并表达想要点餐的意图",
            "询问菜单推荐",
            "选择饮品并说明具体要求",
            "选择小点心",
            "确认订单并付款"
        ],
        background="你正在一家美式咖啡店，需要点一杯咖啡和一份小点心。",
        npc_role="你是一位友好的咖啡店服务员，会帮助顾客点餐并提供建议。",
        learning_objectives=[
            "掌握基本的点餐用语",
            "学习如何询问和表达偏好",
            "练习礼貌用语和日常对话"
        ]
    ),
    "restaurant": Scene(
        id="restaurant",
        title="餐厅用餐",
        description="在餐厅与服务员进行点餐和用餐对话",
        difficulty="intermediate",
        estimated_time=20,
        tasks=[
            "预订座位",
            "查看菜单并询问推荐",
            "点餐并说明特殊要求",
            "处理用餐过程中的问题",
            "结账并给小费"
        ],
        background="你正在一家高档餐厅用餐，需要与服务员进行完整的用餐体验对话。",
        npc_role="你是一位专业的餐厅服务员，熟悉菜单并能提供专业的建议。",
        learning_objectives=[
            "掌握餐厅用餐相关词汇",
            "学习如何表达特殊饮食需求",
            "练习处理用餐过程中的问题"
        ]
    )
}

def get_all_scenes() -> List[Scene]:
    """获取所有场景列表"""
    return list(SCENES.values())

def get_scene(scene_id: str) -> Scene:
    """获取特定场景详情"""
    if scene_id not in SCENES:
        raise ValueError(f"Scene {scene_id} not found")
    return SCENES[scene_id] 