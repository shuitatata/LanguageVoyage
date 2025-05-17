from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import chat
from .core.config import settings
from .db.init_db import init_db

app = FastAPI(title="LanguageVoyage API")

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 初始化数据库
init_db()

# 注册路由
app.include_router(chat.router, prefix=settings.API_V1_STR + "/chat", tags=["chat"])

@app.get("/")
def root():
    return {"message": "Welcome to LanguageVoyage API"} 