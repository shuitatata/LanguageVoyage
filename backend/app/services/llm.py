from typing import List, Optional, Dict
from pydantic import BaseModel
from openai import AsyncOpenAI
from ..core.config import settings

class Message(BaseModel):
    role: str
    content: str

class LLMService:
    def __init__(self):
        """初始化LLM服务"""
        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY,
            base_url=settings.OPENAI_API_BASE_URL
        )
        self.model = settings.OPENAI_MODEL_NAME
        self.temperature = 0.7
        self.max_tokens = 1000

    async def get_chat_response(
        self,
        messages: List[Message],
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
    ) -> str:
        """
        获取LLM的回复
        
        Args:
            messages: 对话历史消息列表
            system_prompt: 系统提示词
            temperature: 温度参数，控制回复的随机性
            
        Returns:
            str: LLM的回复内容
        """
        conversation = []
        
        # 添加系统提示词（如果有）
        if system_prompt:
            conversation.append({
                "role": "system",
                "content": system_prompt
            })
        
        # 添加历史消息
        for msg in messages:
            conversation.append({
                "role": msg.role,
                "content": msg.content
            })
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=conversation,
                temperature=temperature or self.temperature,
                max_tokens=self.max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            # TODO: 添加更详细的错误处理
            raise Exception(f"调用LLM API时发生错误: {str(e)}")

    @staticmethod
    def create_system_prompt(scene_info: Dict) -> str:
        """
        根据场景信息创建系统提示词
        
        Args:
            scene_info: 场景相关信息
            
        Returns:
            str: 格式化的系统提示词
        """
        return f"""你是一个在{scene_info['name']}场景中的{scene_info['npc_role']}。
你需要用{scene_info['language']}与用户进行对话。
场景描述：{scene_info['description']}
你的角色：{scene_info['npc_description']}
难度级别：{scene_info['difficulty']}

请注意：
1. 保持角色设定，用符合场景的语气和用语进行回复
2. 根据用户的语言水平调整回复的难度
3. 如果用户的表达有误，可以适当给出温和的纠正
4. 引导用户完成任务目标，但不要过于直接地告诉答案
""" 