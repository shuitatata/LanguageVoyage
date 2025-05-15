<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import type { Scene } from '@/types/scene'
import { SceneAPI } from '@/api/scenes'

const scenes = ref<Scene[]>([])
const router = useRouter()
const loading = ref(true)

onMounted(async () => {
  try {
    scenes.value = await SceneAPI.getScenes()
  } catch (error) {
    console.error('Failed to load scenes:', error)
  } finally {
    loading.value = false
  }
})

const goToScene = (sceneId: number) => {
  router.push(`/scenes/${sceneId}`)
}
</script>

<template>
  <div class="scene-list">
    <h1>语言学习场景</h1>
    
    <div v-if="loading" class="loading">
      加载中...
    </div>
    
    <div v-else class="scenes-grid">
      <div
        v-for="scene in scenes"
        :key="scene.id"
        class="scene-card"
        @click="goToScene(scene.id)"
      >
        <h2>{{ scene.name }}</h2>
        <p class="description">{{ scene.description }}</p>
        <div class="scene-info">
          <span class="difficulty">难度：{{ scene.difficulty }}</span>
          <span class="time">预计时间：{{ scene.estimated_time }}</span>
        </div>
        <div class="tasks">
          <h3>任务列表：</h3>
          <ul>
            <li v-for="task in scene.tasks" :key="task.id">
              {{ task.description }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.scene-list {
  padding: 2rem;
}

h1 {
  text-align: center;
  margin-bottom: 2rem;
  color: var(--color-heading);
}

.loading {
  text-align: center;
  font-size: 1.2rem;
  margin: 2rem 0;
}

.scenes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  padding: 1rem;
}

.scene-card {
  background: var(--color-background-soft);
  border-radius: 8px;
  padding: 1.5rem;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
  border: 1px solid var(--color-border);
}

.scene-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.scene-card h2 {
  margin: 0 0 1rem;
  color: var(--color-heading);
}

.description {
  color: var(--color-text);
  margin-bottom: 1rem;
}

.scene-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
  font-size: 0.9rem;
  color: var(--color-text-light);
}

.tasks {
  border-top: 1px solid var(--color-border);
  padding-top: 1rem;
}

.tasks h3 {
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

.tasks ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.tasks li {
  font-size: 0.9rem;
  margin: 0.3rem 0;
  color: var(--color-text);
}
</style> 