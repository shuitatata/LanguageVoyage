LanguageVoyage/
├── backend/
│   ├── app/
│   │   ├── api/                    # API路由
│   │   │   ├── __init__.py
│   │   │   ├── auth.py            # 认证相关
│   │   │   ├── scenes.py          # 场景相关
│   │   │   └── users.py           # 用户相关
│   │   ├── core/                   # 核心配置
│   │   │   ├── __init__.py
│   │   │   ├── config.py          # 配置管理
│   │   │   └── security.py        # 安全相关
│   │   ├── models/                 # 数据模型
│   │   │   ├── __init__.py
│   │   │   └── models.py          # 所有模型
│   │   ├── schemas/                # Pydantic模型
│   │   │   ├── __init__.py
│   │   │   └── schemas.py         # 请求响应模型
│   │   └── services/              # 业务逻辑
│   │       ├── __init__.py
│   │       ├── llm.py            # LLM服务
│   │       └── scene.py          # 场景服务
│   ├── tests/                     # 测试文件
│   │   └── test_api/
│   ├── alembic/                   # 数据库迁移
│   │   └── versions/
│   ├── alembic.ini               # Alembic配置
│   ├── main.py                   # 应用入口
│   └── requirements.txt          # 依赖管理
│
├── frontend/
│   ├── src/
│   │   ├── assets/              # 静态资源
│   │   ├── components/          # 通用组件
│   │   │   ├── chat/           # 对话相关组件
│   │   │   └── scene/          # 场景相关组件
│   │   ├── views/              # 页面视图
│   │   │   ├── auth/          # 认证相关页面
│   │   │   ├── scene/         # 场景相关页面
│   │   │   └── user/          # 用户相关页面
│   │   ├── stores/            # Pinia状态管理
│   │   ├── api/               # API调用
│   │   ├── router/            # 路由配置
│   │   ├── types/            # TypeScript类型
│   │   ├── utils/            # 工具函数
│   │   ├── App.vue
│   │   └── main.ts
│   ├── public/
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
│
├── docs/                      # 文档
│   ├── api/                  # API文档
│   └── project_plan.md       # 项目计划
│
├── .github/
│   └── workflows/
│       └── main.yml         # CI/CD配置
│
├── .gitignore
├── README.md
└── LICENSE