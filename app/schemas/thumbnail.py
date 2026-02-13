from pydantic import BaseModel
from typing import Optional, List

class ThumbnailGenerationRequest(BaseModel):
    project_id: int
    category_id: int
    emotion: str
    title_text: str

class ThumbnailOption(BaseModel):
    id: int
    text: str
    placement: Optional[str]
    color_scheme: Optional[str]
    readability_score: Optional[float]
    best_for: Optional[str]