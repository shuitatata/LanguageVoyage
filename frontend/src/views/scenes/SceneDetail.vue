<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import type { Scene } from '@/types/scene'
import { SceneAPI } from '@/api/scenes'

const route = useRoute()
const scene = ref<Scene | null>(null)
const loading = ref(true)
const message = ref('')
const chatHistory = ref<Array<{ role: 'user' | 'assistant', content: string }>>([])
const sessionId = ref<string | null>(null)

// 模型参数设置
const modelSettings = ref({
  temperature: 0.7,
  topP: 0.9,
  presencePenalty: 0,
  frequencyPenalty: 0,
  maxTokens: 1000
})

onMounted(async () => {
  const sceneId = Number(route.params.id)
  try {
    scene.value = await SceneAPI.getScene(sceneId)
    if (scene.value) {
      const session = await SceneAPI.createSession(sceneId)
      sessionId.value = session.session_id
      chatHistory.value.push({ role: 'assistant', content: session.initial_message })
    }
  } catch (error) {
    console.error('Failed to load scene:', error)
  } finally {
    loading.value = false
  }
})

const sendMessage = async () => {
  if (!message.value.trim() || !sessionId.value) return

  const userMessage = message.value
  chatHistory.value.push({ role: 'user', content: userMessage })
  message.value = ''

  try {
    const response = await SceneAPI.sendMessage(sessionId.value, {
      message: userMessage,
      need_task_check: true,
      ...modelSettings.value
    })
    chatHistory.value.push({ role: 'assistant', content: response.reply })
  } catch (error) {
    console.error('Failed to send message:', error)
    chatHistory.value.push({ 
      role: 'assistant', 
      content: '抱歉，发送消息时出现错误。请重试。' 
    })
  }
}
</script>

<template>
  <div class="scene-detail">
    <div v-if="loading" class="loading">
      加载中...
    </div>
    
    <div v-else-if="scene" class="scene-content">
      <div class="scene-header">
        <h1>{{ scene.name }}</h1>
        <div class="scene-info">
          <span class="difficulty">难度：{{ scene.difficulty }}</span>
          <span class="time">预计时间：{{ scene.estimated_time }}</span>
        </div>
      </div>

      <div class="main-content">
        <!-- 左侧：模型参数设置 -->
        <aside class="settings-panel">
          <h2>模型参数设置</h2>
          <div class="setting-item">
            <label>Temperature</label>
            <input 
              type="range" 
              v-model="modelSettings.temperature" 
              min="0" 
              max="1" 
              step="0.1"
            >
            <span>{{ modelSettings.temperature }}</span>
          </div>
          <div class="setting-item">
            <label>Top P</label>
            <input 
              type="range" 
              v-model="modelSettings.topP" 
              min="0" 
              max="1" 
              step="0.1"
            >
            <span>{{ modelSettings.topP }}</span>
          </div>
          <div class="setting-item">
            <label>Presence Penalty</label>
            <input 
              type="range" 
              v-model="modelSettings.presencePenalty" 
              min="-2" 
              max="2" 
              step="0.1"
            >
            <span>{{ modelSettings.presencePenalty }}</span>
          </div>
          <div class="setting-item">
            <label>Frequency Penalty</label>
            <input 
              type="range" 
              v-model="modelSettings.frequencyPenalty" 
              min="-2" 
              max="2" 
              step="0.1"
            >
            <span>{{ modelSettings.frequencyPenalty }}</span>
          </div>
          <div class="setting-item">
            <label>Max Tokens</label>
            <input 
              type="number" 
              v-model="modelSettings.maxTokens" 
              min="100" 
              max="4000"
            >
          </div>

          <div class="scene-description">
            <h3>场景背景</h3>
            <p>{{ scene.background }}</p>
          </div>
        </aside>

        <!-- 中间：聊天区域 -->
        <div class="chat-panel">
          <div class="chat-history" ref="chatContainer">
            <div 
              v-for="(msg, index) in chatHistory" 
              :key="index"
              :class="['message', msg.role]"
            >
              {{ msg.content }}
            </div>
          </div>

          <div class="message-input">
            <input 
              v-model="message"
              @keyup.enter="sendMessage"
              placeholder="输入你的回复..."
              type="text"
            />
            <button @click="sendMessage">发送</button>
          </div>
        </div>

        <!-- 右侧：任务面板 -->
        <aside class="tasks-panel">
          <h2>任务列表</h2>
          <ul>
            <li 
              v-for="task in scene.tasks" 
              :key="task.id"
              :class="{ 'completed': task.status === 'completed' }"
            >
              {{ task.description }}
            </li>
          </ul>
        </aside>
      </div>
    </div>

    <div v-else class="error">
      场景不存在或加载失败
    </div>
  </div>
</template>

<style scoped>
.scene-detail {
  height: calc(100vh - 120px);
  display: flex;
  flex-direction: column;
}

.scene-header {
  padding: 1rem 2rem;
  background: var(--color-background-soft);
  border-bottom: 1px solid var(--color-border);
}

.scene-header h1 {
  margin: 0 0 0.5rem;
  color: var(--color-heading);
}

.scene-info {
  display: flex;
  gap: 1rem;
  color: var(--color-text-light);
}

.main-content {
  flex: 1;
  display: grid;
  grid-template-columns: 300px 1fr 280px;
  gap: 1rem;
  padding: 1rem;
  height: calc(100% - 80px);
  overflow: hidden;
}

/* 左侧面板样式 */
.settings-panel {
  background: var(--color-background-soft);
  border-radius: 8px;
  padding: 1.5rem;
  border: 1px solid var(--color-border);
  overflow-y: auto;
}

.setting-item {
  margin-bottom: 1.5rem;
}

.setting-item label {
  display: block;
  margin-bottom: 0.5rem;
  color: var(--color-text);
  font-weight: 500;
}

.setting-item input[type="range"] {
  width: 100%;
  margin-bottom: 0.5rem;
}

.setting-item input[type="number"] {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid var(--color-border);
  border-radius: 4px;
}

.setting-item span {
  color: var(--color-text-light);
  font-size: 0.9rem;
}

/* 中间聊天区域样式 */
.chat-panel {
  display: flex;
  flex-direction: column;
  background: var(--color-background-soft);
  border-radius: 8px;
  border: 1px solid var(--color-border);
  overflow: hidden;
}

.chat-history {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
}

.message {
  margin: 0.5rem 0;
  padding: 0.8rem;
  border-radius: 8px;
  max-width: 80%;
}

.message.user {
  background: var(--color-background-mute);
  margin-left: auto;
}

.message.assistant {
  background: var(--color-background);
  margin-right: auto;
}

.message-input {
  display: flex;
  gap: 1rem;
  padding: 1rem;
  background: var(--color-background);
  border-top: 1px solid var(--color-border);
}

.message-input input {
  flex: 1;
  padding: 0.8rem;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  background: var(--color-background);
  color: var(--color-text);
}

.message-input button {
  padding: 0.8rem 1.5rem;
  background: var(--color-primary);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: opacity 0.2s;
}

.message-input button:hover {
  opacity: 0.9;
}

/* 右侧任务面板样式 */
.tasks-panel {
  background: var(--color-background-soft);
  border-radius: 8px;
  padding: 1.5rem;
  border: 1px solid var(--color-border);
  overflow-y: auto;
}

.tasks-panel h2 {
  margin-bottom: 1rem;
}

.tasks-panel ul {
  list-style: none;
  padding: 0;
}

.tasks-panel li {
  padding: 0.8rem;
  margin: 0.5rem 0;
  background: var(--color-background-mute);
  border-radius: 4px;
  font-size: 0.9rem;
  transition: background-color 0.2s;
}

.tasks-panel li.completed {
  color: var(--color-text-light);
  text-decoration: line-through;
}

.scene-description {
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid var(--color-border);
}

.scene-description h3 {
  margin-bottom: 0.5rem;
}

.scene-description p {
  font-size: 0.9rem;
  color: var(--color-text);
  line-height: 1.6;
}

.loading, .error {
  text-align: center;
  padding: 2rem;
  font-size: 1.2rem;
}
</style> 