from pydantic import BaseModel
from typing import List, Optional

class DescriptionGenerationRequest(BaseModel):
    category_id: int
    niche: str
    pattern_name: str
    success_rate: float
    avg_multiplier: float
    chapters: List[tuple]  # [(timestamp, title), ...]
    equipment: List[str]
    cta_text: str