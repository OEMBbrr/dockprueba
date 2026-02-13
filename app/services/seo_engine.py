import re
from sqlalchemy.orm import Session
from app.models import Category
from app.schemas.seo import TagGenerationRequest

class SEOEngine:
    @staticmethod
    def generate_tags(db: Session, request: TagGenerationRequest) -> list[str]:
        primary = []
        category = db.query(Category).filter(Category.id == request.category_id).first()
        if category:
            primary.append(category.name.lower())
        words = re.findall(r'\b[A-Za-z0-9]+\b', request.title_text.lower())
        primary.extend(words[:3])

        secondary = [f"{w} {category.name.lower()}" for w in words[:2]] if category else []
        long_tail = request.technical_specs[:3]
        all_tags = list(set(primary + secondary + long_tail))[:15]
        return all_tags

    @staticmethod
    def generate_hashtags(tags: list[str]) -> list[str]:
        return [f"#{tag.replace(' ', '')}" for tag in tags[:8]]