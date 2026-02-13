from pydantic import BaseModel
from typing import List, Optional

class TitleGenerationRequest(BaseModel):
    topic: str
    category_id: Optional[int] = None
    target_emotions: List[str] = []
    technical_level: str = "intermediate"
    channel_average_views: Optional[int] = None
    subscriber_count: Optional[int] = None

class TitleSuggestion(BaseModel):
    pattern_id: int
    pattern_name: str
    template: str
    generated_variant: str
    examples: List[str]
    estimated_ctr: str
    avg_multiplier: float
    psychological_triggers: List[str]
    score: int

class TitleSelection(BaseModel):
    project_id: int
    title_id: int