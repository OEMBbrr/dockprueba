from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.image_generator import ImageGenerationService
from app.models import Project

router = APIRouter()

@router.post("/generate-image")
async def generate_image(project_id: int, platform: str = "dalle", db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project or not project.image_prompt:
        raise HTTPException(status_code=400, detail="Prompt no disponible")
    service = ImageGenerationService(db)
    if platform == "dalle":
        result = await service.generate_image_dalle(project.image_prompt)
    else:
        raise HTTPException(status_code=400, detail="Plataforma no soportada")
    return result