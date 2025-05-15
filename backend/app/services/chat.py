import uuid
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from ..models.models import ChatSession, ChatMessage
from ..schemas.chat import ChatMessageCreate

class ChatService:
    @staticmethod
    def create_session(db: Session, scene_id: int) -> ChatSession:
        """创建新的对话会话"""
        session_id = str(uuid.uuid4())
        session = ChatSession(session_id=session_id, scene_id=scene_id)
        db.add(session)
        db.commit()
        db.refresh(session)
        return session

    @staticmethod
    def get_chat_history(db: Session, session_id: str) -> List[ChatMessage]:
        """获取会话历史记录"""
        messages = db.query(ChatMessage).filter(
            ChatMessage.session_id == session_id
        ).order_by(ChatMessage.created_at).all()
        return messages

    @staticmethod
    def process_message(db: Session, message: ChatMessageCreate) -> ChatMessage:
        """处理新消息"""
        # 创建用户消息
        user_message = ChatMessage(
            content=message.content,
            session_id=message.session_id,
            role="user"
        )
        db.add(user_message)
        
        # TODO: 调用 LLM 生成回复
        assistant_response = "这是一个模拟的助手回复"
        assistant_message = ChatMessage(
            content=assistant_response,
            session_id=message.session_id,
            role="assistant"
        )
        db.add(assistant_message)
        
        db.commit()
        db.refresh(assistant_message)
        return assistant_message 