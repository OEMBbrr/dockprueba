import json
from typing import Any, Optional
from sqlalchemy.orm import Session
from app.models import ViralPattern, TitleExample
from app.schemas.title import TitleGenerationRequest

def safe_json_parse(data: Any) -> Any:
    """
    Convierte un campo JSON de la base de datos a un objeto Python.
    Si ya es dict/list, lo devuelve; si es string, lo parsea con json.loads.
    """
    if data is None:
        return None
    if isinstance(data, (dict, list)):
        return data
    if isinstance(data, str):
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            return data  # fallback: devolver el string original
    return data  # otro tipo, devolver tal cual

class TitleEngine:
    @staticmethod
    def generate_titles(db: Session, request: TitleGenerationRequest) -> list[dict]:
        query = db.query(ViralPattern)
        if request.category_id:
            query = query.filter(ViralPattern.category_id == request.category_id)
        patterns = query.all()

        scored = []
        for p in patterns:
            triggers = safe_json_parse(p.psychological_triggers)
            score = 0
            if triggers and isinstance(triggers, list):
                for t in request.target_emotions:
                    if t in triggers:
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
                "psychological_triggers": safe_json_parse(pattern.psychological_triggers) or [],
                "score": score
            })
        return generated