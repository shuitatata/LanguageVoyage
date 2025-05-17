from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import scenes

app = FastAPI(title="LanguageVoyage API")

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在开发环境中允许所有来源
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(scenes.router)

@app.get("/")
async def root():
    return {"message": "Welcome to LanguageVoyage API"} 