from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class ProjectCreate(BaseModel):
    user_id: str
    topic: str
    emotion: Optional[str] = None
    technical_level: Optional[str] = None

class ProjectOut(BaseModel):
    id: int
    user_id: str
    topic: str
    emotion: Optional[str]
    technical_level: Optional[str]
    status: str
    selected_title_id: Optional[int]
    selected_thumbnail_copy_id: Optional[int]
    image_prompt: Optional[str]
    generated_description: Optional[str]
    tags: Optional[List[str]]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True