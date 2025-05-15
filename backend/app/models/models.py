from sqlalchemy import Column, Integer, String, Text, DateTime, func
from ..db.database import Base

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