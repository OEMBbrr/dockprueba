from sqlalchemy.orm import Session
from app.models import ViralPattern, TitleExample
from app.schemas.title import TitleGenerationRequest
import json

class TitleEngine:
    @staticmethod
    def generate_titles(db: Session, request: TitleGenerationRequest) -> list[dict]:
        query = db.query(ViralPattern)
        if request.category_id:
            query = query.filter(ViralPattern.category_id == request.category_id)
        patterns = query.all()

        scored = []
        for p in patterns:
            triggers = p.psychological_triggers
            score = 0
            if triggers:
                trig_list = json.loads(triggers) if isinstance(triggers, str) else triggers
                for t in request.target_emotions:
                    if t in trig_list:
                        score += 10
            scored.append((p, score))

        scored.sort(key=lambda x: x[1], reverse=True)

        generated = []
        for pattern, _ in scored[:5]:
            template = pattern.pattern_template
            # Sustituciones de ejemplo (en producción se harían con NLP o placeholders reales)
            replacements = {
                "[Sistema/Componente]": "Sistema",
                "[Marca]": "Ferrari",
                "[Tiempo]": "2024",
                "[Razón Técnica]": "explotar un vacío legal",
                "[Underdog]": "Brawn GP",
                "[Gigante]": "Ferrari",
                "[Competición]": "F1",
                "[Prototipo/Proyecto]": "Prototipo",
            }
            for key, val in replacements.items():
                if key in template:
                    template = template.replace(key, val)

            examples_q = db.query(TitleExample).filter(
                TitleExample.viral_pattern_id == pattern.id
            ).limit(3).all()
            example_texts = [ex.title_text for ex in examples_q]

            generated.append({
                "pattern_id": pattern.id,
                "pattern_name": pattern.name,
                "template": pattern.pattern_template,
                "generated_variant": template,
                "examples": example_texts,
                "estimated_ctr": f"{pattern.ctr_range_min}-{pattern.ctr_range_max}%",
                "avg_multiplier": pattern.avg_multiplier,
                "psychological_triggers": json.loads(pattern.psychological_triggers) if pattern.psychological_triggers else [],
                "score": score
            })
        return generated