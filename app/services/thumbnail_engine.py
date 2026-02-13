from sqlalchemy.orm import Session
from app.models import ThumbnailCopy
from app.schemas.thumbnail import ThumbnailGenerationRequest

class ThumbnailEngine:
    @staticmethod
    def generate_copy_options(db: Session, request: ThumbnailGenerationRequest) -> list[dict]:
        query = db.query(ThumbnailCopy).filter(ThumbnailCopy.category_id == request.category_id)
        copies = query.limit(10).all()
        options = []
        for copy in copies:
            options.append({
                "id": copy.id,
                "text": copy.text,
                "placement": copy.placement.value if copy.placement else None,
                "color_scheme": copy.color_scheme,
                "readability_score": copy.readability_score,
                "best_for": copy.best_for
            })
        return options[:5]