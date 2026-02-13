from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.title_engine import TitleEngine
from app.schemas.title import TitleGenerationRequest, TitleSuggestion, TitleSelection
from app.models import Project, TitleExample

router = APIRouter()

@router.post("/generate", response_model=list[TitleSuggestion])
def generate_titles(request: TitleGenerationRequest, db: Session = Depends(get_db)):
    engine = TitleEngine()
    suggestions = engine.generate_titles(db, request)
    return suggestions

@router.post("/select")
def select_title(selection: TitleSelection, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == selection.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    title = db.query(TitleExample).filter(TitleExample.id == selection.title_id).first()
    if not title:
        raise HTTPException(status_code=404, detail="Título no encontrado")
    project.selected_title_id = title.id
    project.status = "title_selected"
    db.commit()
    return {"message": "Título seleccionado", "project_id": project.id}