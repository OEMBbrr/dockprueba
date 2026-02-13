from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.seo_engine import SEOEngine
from app.schemas.seo import TagGenerationRequest

router = APIRouter()

@router.post("/tags/generate")
def generate_tags(request: TagGenerationRequest, db: Session = Depends(get_db)):
    engine = SEOEngine()
    tags = engine.generate_tags(db, request)
    hashtags = engine.generate_hashtags(tags)
    return {"tags": tags, "hashtags": hashtags}