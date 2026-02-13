from pydantic import BaseModel
from typing import List, Optional

class TagGenerationRequest(BaseModel):
    category_id: int
    title_text: str
    technical_specs: List[str] = []