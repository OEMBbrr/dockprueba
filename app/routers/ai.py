from fastapi import APIRouter, HTTPException
from app.services.google_ai import GoogleAIService
from pydantic import BaseModel

router = APIRouter()

class TitleVariantRequest(BaseModel):
    topic: str
    emotion: str
    count: int = 3

class CopyVariantRequest(BaseModel):
    title: str
    emotion: str
    count: int = 3

@router.post("/titles/generate-ai")
def generate_title_variants(req: TitleVariantRequest):
    service = GoogleAIService()
    variants = service.generate_title_variants(req.topic, req.emotion, req.count)
    if not variants:
        raise HTTPException(status_code=503, detail="Gemini API no disponible o sin clave")
    return {"variants": variants}

@router.post("/thumbnails/generate-ai")
def generate_copy_variants(req: CopyVariantRequest):
    service = GoogleAIService()
    variants = service.generate_thumbnail_copy_variants(req.title, req.emotion, req.count)
    if not variants:
        raise HTTPException(status_code=503, detail="Gemini API no disponible")
    return {"variants": variants}