from fastapi import APIRouter, HTTPException
from app.services.youtube_analytics import YouTubeService
from pydantic import BaseModel

router = APIRouter()

class VideoRequest(BaseModel):
    video_id: str

@router.post("/stats")
def get_video_stats(req: VideoRequest):
    service = YouTubeService()
    stats = service.get_video_stats(req.video_id)
    if not stats:
        raise HTTPException(status_code=404, detail="Video no encontrado o API no configurada")
    return stats