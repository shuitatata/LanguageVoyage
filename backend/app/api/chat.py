from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas.chat import (
    ChatMessageCreate,
    ChatMessageResponse,
    ChatHistoryResponse,
    ChatSessionCreate,
    ChatSessionResponse
)
from ..services.chat import ChatService
from ..db.database import get_db

router = APIRouter()

@router.post("/sessions", response_model=ChatSessionResponse)
def create_chat_session(
    session: ChatSessionCreate,
    db: Session = Depends(get_db)
):
    """创建新的对话会话"""
    db_session = ChatService.create_session(db, session.scene_id)
    return db_session

@router.get("/sessions/{session_id}/history", response_model=ChatHistoryResponse)
def get_chat_history(
    session_id: str,
    db: Session = Depends(get_db)
):
    """获取会话历史记录"""
    messages = ChatService.get_chat_history(db, session_id)
    return {"session_id": session_id, "messages": messages}

@router.post("/chat", response_model=ChatMessageResponse)
def chat(
    message: ChatMessageCreate,
    db: Session = Depends(get_db)
):
    """处理用户消息并返回 AI 响应"""
    return ChatService.process_message(db, message) 