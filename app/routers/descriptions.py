from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.description_engine import DescriptionEngine
from app.schemas.description import DescriptionGenerationRequest

router = APIRouter()

@router.post("/generate")
def generate_description(request: DescriptionGenerationRequest, db: Session = Depends(get_db)):
    engine = DescriptionEngine()
    description = engine.build_description(db, request)
    return {"description": description}