from fastapi import APIRouter, HTTPException
from typing import List
from ..models.scene import Scene
from ..services.scene_service import get_all_scenes, get_scene

router = APIRouter(prefix="/api/scenes", tags=["scenes"])

@router.get("/", response_model=List[Scene])
async def list_scenes():
    """获取所有场景列表"""
    return get_all_scenes()

@router.get("/{scene_id}", response_model=Scene)
async def get_scene_by_id(scene_id: str):
    """获取特定场景详情"""
    try:
        return get_scene(scene_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) 