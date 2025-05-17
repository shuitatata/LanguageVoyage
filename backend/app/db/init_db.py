from .database import engine, Base, SessionLocal
from ..models.models import ChatSession, ChatMessage, Scene
from .seed import seed_scenes

def init_db():
    """初始化数据库，创建所有表并添加种子数据"""
    # 创建所有表
    Base.metadata.create_all(bind=engine)
    
    # 添加种子数据
    db = SessionLocal()
    try:
        seed_scenes(db)
    finally:
        db.close() 
