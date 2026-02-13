from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.thumbnail_engine import ThumbnailEngine
from app.schemas.thumbnail import ThumbnailGenerationRequest, ThumbnailOption
from app.models import Project, ThumbnailCopy

router = APIRouter()

@router.post("/generate", response_model=list[ThumbnailOption])
def generate_thumbnails(request: ThumbnailGenerationRequest, db: Session = Depends(get_db)):
    engine = ThumbnailEngine()
    options = engine.generate_copy_options(db, request)
    return options

@router.post("/select")
def select_thumbnail(project_id: int, thumbnail_copy_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    copy = db.query(ThumbnailCopy).filter(ThumbnailCopy.id == thumbnail_copy_id).first()
    if not copy:
        raise HTTPException(status_code=404, detail="Copia no encontrada")
    project.selected_thumbnail_copy_id = copy.id
    project.status = "thumbnail_selected"
    db.commit()
    return {"message": "Copia de miniatura seleccionada"}