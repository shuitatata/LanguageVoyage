import { createRouter, createWebHistory } from 'vue-router'
import SceneList from '../views/scenes/SceneList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: SceneList,
    },
    {
      path: '/scenes',
      name: 'scenes',
      component: SceneList,
    },
    {
      path: '/scenes/:id',
      name: 'scene-detail',
      component: () => import('../views/scenes/SceneDetail.vue'),
    },
  ],
})

export default router
