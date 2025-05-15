export interface Scene {
  id: number
  name: string
  description: string
  difficulty: string
  estimated_time: string
  tasks: Task[]
  background: string
  npc_role: string
  learning_objectives: string[]
}

export interface Task {
  id: string
  description: string
  status: 'pending' | 'completed'
  completed_at: string | null
}

export interface TaskProgress {
  completed: number
  total: number
}

export interface Session {
  session_id: string
  scene_info: Scene
  initial_message: string
}

export interface Message {
  message: string
  need_task_check?: boolean
  temperature?: number
}

export interface MessageResponse {
  reply: string
  task_progress?: {
    completed_tasks: string[]
    next_task: string
  }
}

export interface Feedback {
  grammar_corrections: Array<{
    original: string
    correction: string
    explanation: string
  }>
  vocabulary_suggestions: Array<{
    word: string
    context: string
    alternatives: string[]
  }>
  overall_feedback: string
} 