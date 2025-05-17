from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List, Optional

class ChatMessageCreate(BaseModel):
    content: str
    session_id: str
    scene_id: Optional[int] = None  # 仅在创建新会话时需要

class ChatMessageResponse(BaseModel):
    id: int
    content: str
    role: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class ChatHistoryResponse(BaseModel):
    session_id: str
    messages: List[ChatMessageResponse]

class ChatSessionCreate(BaseModel):
    scene_id: int

class ChatSessionResponse(BaseModel):
    session_id: str
    scene_id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True) 