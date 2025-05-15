from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # SQLite 数据库配置
    DATABASE_URL: str = "sqlite:///./language_voyage.db"
    
    # API配置
    API_V1_STR: str = "/api/v1"
    
    class Config:
        env_file = ".env"

settings = Settings() 