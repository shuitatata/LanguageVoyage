from pydantic import BaseModel
from typing import List, Optional

class Scene(BaseModel):
    id: str
    title: str
    description: str
    difficulty: str  # "beginner", "intermediate", "advanced"
    estimated_time: int  # 预计完成时间（分钟）
    tasks: List[str]
    background: str  # 场景背景描述
    npc_role: str  # NPC 角色描述
    learning_objectives: List[str]  # 学习目标 