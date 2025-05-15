# LanguageVoyage

基于LLM的情景式语言学习应用 - 通过真实场景对话提升语言能力

## 项目简介

LanguageVoyage 是一个创新的语言学习平台，通过模拟真实生活场景，结合大语言模型（LLM）的对话能力，为用户提供沉浸式的语言学习体验。用户可以在各种预设场景中与AI进行对话，完成特定任务，从而提升语言应用能力。

## 核心特性

- 🎯 **场景化学习**：提供多个真实生活场景，让语言学习更贴近实际
- 🤖 **智能对话**：基于LLM的NPC角色扮演，提供自然流畅的对话体验
- ✅ **任务系统**：通过完成场景任务，循序渐进地提升语言能力
- 💡 **智能提示**：多级提示系统，在遇到困难时提供适当帮助
- 📝 **学习反馈**：实时语法纠正和表达优化建议

## 技术栈

### 前端
- Vue 3
- Vue Router
- Pinia
- Element Plus

### 后端
- FastAPI
- SQLAlchemy
- PostgreSQL
- LangChain

## 开发环境要求

- Python 3.12+
- Node.js 18+
- PostgreSQL 14+

## 快速开始

1. 克隆项目
```bash
git clone https://github.com/yourusername/LanguageVoyage.git
cd LanguageVoyage
```

2. 后端设置
```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows使用: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 启动后端服务
cd backend
uvicorn main:app --reload
```

3. 前端设置
```bash
# 安装依赖
cd frontend
npm install

# 启动开发服务器
npm run dev
```

## 项目结构

```
LanguageVoyage/
├── backend/             # 后端代码
│   ├── app/            # 应用代码
│   ├── tests/          # 测试文件
│   └── requirements.txt # Python依赖
├── frontend/           # 前端代码
│   ├── src/           # 源代码
│   ├── public/        # 静态资源
│   └── package.json   # Node.js依赖
└── docs/              # 项目文档
```

## 贡献指南

欢迎贡献代码！请确保在提交PR前：

1. 代码符合项目规范
2. 添加必要的测试
3. 更新相关文档

## 开源许可

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件 