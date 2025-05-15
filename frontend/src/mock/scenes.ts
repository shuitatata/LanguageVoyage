import type { Scene } from '../types/scene';

export const mockScenes: Scene[] = [
    {
        id: 1,
        name: "咖啡店点餐",
        description: "在美式咖啡店与服务员交流完成点餐",
        difficulty: "初级",
        estimated_time: "15分钟",
        background: "你正在美国旅游，来到一家当地很受欢迎的咖啡店。这是一个练习日常英语对话的好机会。",
        npc_role: "友好的咖啡店服务员",
        learning_objectives: [
            "掌握点餐相关词汇",
            "学习礼貌用语",
            "练习表达个人偏好"
        ],
        tasks: [
            {
                id: "task1",
                description: "向服务员问候",
                status: "pending",
                completed_at: null
            },
            {
                id: "task2",
                description: "询问菜单推荐",
                status: "pending",
                completed_at: null
            },
            {
                id: "task3",
                description: "点餐并说明具体要求",
                status: "pending",
                completed_at: null
            },
            {
                id: "task4",
                description: "确认订单并付款",
                status: "pending",
                completed_at: null
            }
        ]
    },
    {
        id: 2,
        name: "机场值机",
        description: "在机场办理值机手续并托运行李",
        difficulty: "中级",
        estimated_time: "20分钟",
        background: "你即将搭乘国际航班，需要在机场办理值机手续。这是练习机场相关英语对话的绝佳机会。",
        npc_role: "机场值机柜台工作人员",
        learning_objectives: [
            "掌握机场相关词汇",
            "学习预订和值机用语",
            "练习处理突发情况"
        ],
        tasks: [
            {
                id: "task1",
                description: "找到正确的值机柜台",
                status: "pending",
                completed_at: null
            },
            {
                id: "task2",
                description: "出示护照和订票信息",
                status: "pending",
                completed_at: null
            },
            {
                id: "task3",
                description: "选择座位",
                status: "pending",
                completed_at: null
            },
            {
                id: "task4",
                description: "托运行李",
                status: "pending",
                completed_at: null
            },
            {
                id: "task5",
                description: "获取登机牌",
                status: "pending",
                completed_at: null
            }
        ]
    }
]; 