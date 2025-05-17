from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # SQLite 数据库配置
    DATABASE_URL: str = "sqlite:///./language_voyage.db"
    
    # API配置
    API_V1_STR: str = "/api/v1"
    
    # OpenAI配置
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    OPENAI_API_BASE_URL: str = os.getenv("OPENAI_API_BASE_URL")
    OPENAI_MODEL_NAME: str = "deepseek-ai/DeepSeek-V3"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings() 