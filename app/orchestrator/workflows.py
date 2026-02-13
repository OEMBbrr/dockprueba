import json
from sqlalchemy.orm import Session
from app.models import WorkflowInstance, ProductionWorkflow, Project
from app.services.title_engine import TitleEngine
from app.services.thumbnail_engine import ThumbnailEngine
from app.services.description_engine import DescriptionEngine
from app.services.seo_engine import SEOEngine
from app.services.image_generator import ImageGenerationService

class WorkflowOrchestrator:
    def __init__(self, db: Session):
        self.db = db

    def process_step(self, instance: WorkflowInstance, step_id: str, step_inputs: dict):
        workflow = instance.workflow
        steps = json.loads(workflow.steps) if isinstance(workflow.steps, str) else workflow.steps
        current_step = next((s for s in steps if s["id"] == step_id), None)
        if not current_step:
            raise ValueError(f"Paso {step_id} no encontrado")

        next_step_id = self._execute_logic(instance, current_step, step_inputs)

        instance.current_step_id = next_step_id
        if not next_step_id:
            instance.status = "completed"
        current_data = instance.data or {}
        current_data.update(step_inputs)
        instance.data = current_data
        self.db.commit()
        return next_step_id

    def _execute_logic(self, instance: WorkflowInstance, step: dict, inputs: dict):
        step_id = step["id"]
        project_id = instance.data.get("project_id")
        project = self.db.query(Project).filter(Project.id == project_id).first()

        if step_id == "extract_script":
            # Aquí se analizaría el script y se extraerían metadatos
            project.technical_level = "advanced"
            project.emotion = "controversia"
            self.db.commit()
            return step["next"]["default"]

        elif step_id == "generate_titles":
            from app.schemas.title import TitleGenerationRequest
            req = TitleGenerationRequest(
                topic=project.topic,
                category_id=1,
                target_emotions=[project.emotion] if project.emotion else [],
                technical_level=project.technical_level or "intermediate"
            )
            engine = TitleEngine()
            suggestions = engine.generate_titles(self.db, req)
            instance.data["title_suggestions"] = suggestions
            return step["next"]["default"]

        elif step_id == "select_title":
            return step["next"]["default"]

        elif step_id == "generate_thumbnail_copy":
            from app.schemas.thumbnail import ThumbnailGenerationRequest
            req = ThumbnailGenerationRequest(
                project_id=project.id,
                category_id=1,
                emotion=project.emotion or "curiosidad",
                title_text=project.selected_title.title_text if project.selected_title else ""
            )
            engine = ThumbnailEngine()
            options = engine.generate_copy_options(self.db, req)
            instance.data["thumbnail_options"] = options
            return step["next"]["default"]

        elif step_id == "select_thumbnail_copy":
            return step["next"]["default"]

        elif step_id == "generate_image_direct":
            image_svc = ImageGenerationService(self.db)
            platform = "Midjourney"
            prompt = image_svc.compile_prompt(
                platform=platform,
                subject=project.topic,
                environment="circuito",
                lighting="cinematográfica",
                composition="primer plano",
                text_overlay=project.selected_thumbnail_copy.text if project.selected_thumbnail_copy else ""
            )
            project.image_prompt = prompt
            self.db.commit()
            return step["next"]["default"]

        elif step_id == "generate_seo":
            from app.schemas.seo import TagGenerationRequest
            seo_engine = SEOEngine()
            tags = seo_engine.generate_tags(self.db, TagGenerationRequest(
                category_id=1,
                title_text=project.selected_title.title_text if project.selected_title else "",
                technical_specs=[]
            ))
            project.tags = tags
            self.db.commit()
            return step["next"]["default"]

        elif step_id == "complete":
            project.status = "completed"
            self.db.commit()
            return None
        else:
            return step["next"].get("default")