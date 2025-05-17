import uuid
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from ..models.models import ChatSession, ChatMessage, Scene
from ..schemas.chat import ChatMessageCreate
from .llm import LLMService, Message
from fastapi import HTTPException

class ChatService:
    def __init__(self):
        """初始化聊天服务"""
        self.llm_service = LLMService()

    @staticmethod
    def create_session(db: Session, scene_id: int) -> ChatSession:
        """创建新的对话会话"""
        # 检查场景是否存在
        scene = db.query(Scene).filter(Scene.id == scene_id).first()
        if not scene:
            raise HTTPException(status_code=404, detail=f"Scene {scene_id} not found")
            
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


    async def process_message(self, db: Session, message: ChatMessageCreate) -> ChatMessage:
        """处理新消息"""
        # 创建用户消息
        user_message = ChatMessage(
            content=message.content,
            session_id=message.session_id,
            role="user"
        )
        db.add(user_message)
        
        # 获取场景信息
        session = db.query(ChatSession).filter(
            ChatSession.session_id == message.session_id
        ).first()
        if not session:
            raise HTTPException(status_code=404, detail=f"Session {message.session_id} not found")
            
        scene = db.query(Scene).filter(Scene.id == session.scene_id).first()
        if not scene:
            raise HTTPException(status_code=404, detail=f"Scene {session.scene_id} not found")
        
        # 获取历史消息
        history = self.get_chat_history(db, message.session_id)
        messages = [Message(role=msg.role, content=msg.content) for msg in history]
        messages.append(user_message)
        
        # 创建系统提示词
        scene_info = {
            "name": scene.name,
            "description": scene.description,
            "language": scene.language,
            "npc_role": scene.npc_role,
            "npc_description": scene.npc_description,
            "difficulty": scene.difficulty.value,
            "tasks": scene.tasks,
            "tasks_info": scene.tasks_info
        }
        system_prompt = self.llm_service.create_system_prompt(scene_info)
        
        # 调用LLM获取回复
        assistant_response = await self.llm_service.get_chat_response(
            messages=messages,
            system_prompt=system_prompt
        )
        
        # 保存助手回复
        assistant_message = ChatMessage(
            content=assistant_response,
            session_id=message.session_id,
            role="assistant"
        )
        db.add(assistant_message)
        
        db.commit()
        db.refresh(assistant_message)
        return assistant_message 