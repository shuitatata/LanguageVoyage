from sqlalchemy import Column, Integer, String, Text, DateTime, func, Enum
from ..db.database import Base
import enum

class DifficultyLevel(str, enum.Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class Scene(Base):
    __tablename__ = "scenes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)  # 场景名称
    description = Column(Text)  # 场景描述
    language = Column(String(50))  # 场景使用的语言
    npc_role = Column(String(100))  # NPC角色
    npc_description = Column(Text)  # NPC角色描述
    difficulty = Column(Enum(DifficultyLevel))  # 难度级别
    tasks = Column(Text)  # 任务列表（JSON格式）
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class ChatSession(Base):
    __tablename__ = "chat_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(50), unique=True, index=True)  # 唯一会话ID
    scene_id = Column(Integer)  # 场景ID，后续可以添加外键关联
    created_at = Column(DateTime, server_default=func.now())
    last_updated = Column(DateTime(timezone=True), onupdate=func.now())

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(50), index=True)
    content = Column(Text)
    role = Column(String(20))  # user 或 assistant
    created_at = Column(DateTime, server_default=func.now()) 