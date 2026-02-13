from sqlalchemy.orm import Session
from app.models import DescriptionTemplate
from app.schemas.description import DescriptionGenerationRequest

class DescriptionEngine:
    @staticmethod
    def build_description(db: Session, request: DescriptionGenerationRequest) -> str:
        template = db.query(DescriptionTemplate).filter(
            DescriptionTemplate.category_id == request.category_id
        ).first()
        if not template:
            template = db.query(DescriptionTemplate).first()
        if not template:
            return "Descripción por defecto."

        desc = template.template_text
        placeholders = {
            "{dataset}": "10,000",
            "{niche}": request.niche,
            "{pattern}": request.pattern_name,
            "{success_rate}": str(request.success_rate),
            "{multiplier}": str(request.avg_multiplier),
            "{chapters}": "\n".join([f"{t} - {title}" for t, title in request.chapters]),
            "{equipment}": "\n".join([f"• {e}" for e in request.equipment]),
            "{cta}": request.cta_text,
        }
        for key, val in placeholders.items():
            desc = desc.replace(key, val)
        return desc