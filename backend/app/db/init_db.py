from .database import engine, Base
from ..models.models import ChatSession, ChatMessage

def init_db():
    """初始化数据库，创建所有表"""
    Base.metadata.create_all(bind=engine) 