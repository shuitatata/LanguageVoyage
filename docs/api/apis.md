# 场景API
GET /api/scenes
- 获取所有场景列表
- 响应：场景列表，包含基本信息（id, title, description, difficulty）

GET /api/scenes/{scene_id}
- 获取特定场景详情
- 响应：完整场景信息，包括任务列表、背景描述等

# 学习会话API
POST /api/sessions
- 创建新的学习会话
- 请求体：
  ```json
  {
    "scene_id": "string",
    "language_level": "string",  // 可选，用户语言水平
    "target_language": "string"  // 学习目标语言
  }
  ```
- 响应：
  ```json
  {
    "session_id": "string",
    "scene_info": {
      // 场景详细信息
    },
    "initial_message": "string"  // NPC的开场白
  }
  ```

GET /api/sessions/{session_id}
- 获取会话信息
- 响应：会话的详细信息，包括场景信息、进度等

GET /api/sessions
- 获取用户的所有学习会话
- 查询参数：
  - status: "active" | "completed" | "all"
  - scene_id: string (可选)
- 响应：会话列表

# 对话API
POST /api/sessions/{session_id}/messages
- 发送对话消息
- 请求体：
  ```json
  {
    "message": "string",
    "need_task_check": boolean, // 是否需要检查任务进度
    // 是的话则根据对话历史记录检查
    // 否的话则单独检查
    "temperature": float, // 温度参数，用于控制回复的随机性
    ... // 其他 LLM 参数
  }
  ```
- 响应：
  ```json
  {
    "reply": "string",  // NPC回复
    },
    "task_progress": {  // 如果need_task_check为true，则返回任务进度，否则为null
      "completed_tasks": ["task_id"],
      "next_task": "task_id"
    }
  }
  ```

GET /api/sessions/{session_id}/messages
- 获取会话的对话历史
- 响应：对话消息列表

POST /api/sessions/{session_id}/end
- 结束学习会话
- 响应：会话总结信息

PUT /api/sessions/{session_id}/pause
- 暂停会话
- 响应：当前会话状态

# 任务API
GET /api/sessions/{session_id}/tasks
- 获取当前会话的任务列表和进度
- 响应：
  ```json
  {
    "tasks": [
      {
        "id": "string",
        "description": "string",
        "status": "pending" | "completed",
        "completed_at": "datetime" | null
      }
    ],
    "progress": {
      "completed": number,
      "total": number
    }
  }
  ```

POST /api/sessions/{session_id}/tasks/{task_id}/check
- 检查任务进度
- 请求体：
  ```json
  {
    "task_id": "string",
    "scene_id": "string",
    "user_answer": "string"
  }
  ```
- 响应：
  ```json
  {
    "is_correct": boolean,
    "explanation": "string"
  }
  ```

# 帮助API
POST /api/sessions/{session_id}/hints
- 获取对话帮助
- 请求体：
  ```json
  {
    "message": "string"
  }

POST /api/sessions/{session_id}/tasks/{task_id}/hints
- 获取任务帮助
- 请求体：
  ```json
  {
    "message": "string"
  }


# 学习反馈API
GET /api/sessions/{session_id}/feedback
- 获取学习反馈
- 响应：
  ```json
  {
    "grammar_corrections": [
      {
        "original": "string",
        "correction": "string",
        "explanation": "string"
      }
    ],
    "vocabulary_suggestions": [
      {
        "word": "string",
        "context": "string",
        "alternatives": ["string"]
      }
    ],
    "overall_feedback": "string"
  }
  ```

