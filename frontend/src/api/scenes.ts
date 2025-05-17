import type { Scene, Session, Message, MessageResponse, Feedback } from '../types/scene';
import { mockScenes } from '../mock/scenes';

// 模拟 API 延迟
const delay = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

export class SceneAPI {
    // 获取所有场景
    static async getScenes(): Promise<Scene[]> {
        await delay(500); // 模拟网络延迟
        return mockScenes;
    }

    // 获取特定场景
    static async getScene(id: number): Promise<Scene | null> {
        await delay(300);
        return mockScenes.find(scene => scene.id === id) || null;
    }

    // 创建学习会话
    static async createSession(sceneId: number): Promise<Session> {
        await delay(800);
        const scene = await this.getScene(sceneId);
        if (!scene) {
            throw new Error('Scene not found');
        }

        return {
            session_id: `session_${Date.now()}`,
            scene_info: scene,
            initial_message: `你好！我是${scene.npc_role}。欢迎来到${scene.name}场景。让我们开始对话吧！`
        };
    }

    // 发送消息
    static async sendMessage(sessionId: string, message: Message): Promise<MessageResponse> {
        await delay(1000);
        console.log('Sending message:', { sessionId, message }); // 添加日志
        return {
            reply: "这是一个模拟的回复消息。在实际环境中，这里会返回 AI 生成的回复。",
            task_progress: {
                completed_tasks: ["task1"],
                next_task: "task2"
            }
        };
    }

    // 获取学习反馈
    static async getFeedback(sessionId: string): Promise<Feedback> {
        await delay(800);
        console.log('Getting feedback for session:', sessionId); // 添加日志
        return {
            grammar_corrections: [
                {
                    original: "I wants a coffee",
                    correction: "I want a coffee",
                    explanation: "第三人称单数时才需要在动词后加's'"
                }
            ],
            vocabulary_suggestions: [
                {
                    word: "coffee",
                    context: "ordering drinks",
                    alternatives: ["espresso", "latte", "cappuccino"]
                }
            ],
            overall_feedback: "整体表现不错！注意动词变位的使用。"
        };
    }
} 