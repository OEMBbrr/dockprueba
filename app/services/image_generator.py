import requests
from sqlalchemy.orm import Session
from app.models import PlatformSyntax
from app.core.config import settings

class ImageGenerationService:
    def __init__(self, db: Session):
        self.db = db

    def compile_prompt(self, platform: str, subject: str, environment: str, lighting: str, composition: str, text_overlay: str = None, reference_image: str = None) -> str:
        syntax = self.db.query(PlatformSyntax).filter(
            PlatformSyntax.platform_name.ilike(f"%{platform}%")
        ).first()
        if not syntax:
            base = f"{subject} in {environment}, {lighting}, {composition}"
        else:
            base = syntax.syntax_template
            base = base.replace("[Subject]", subject)
            base = base.replace("[Environment]", environment)
            base = base.replace("[Lighting/Mood]", lighting)
            base = base.replace("[Camera/Lens]", composition)
            if text_overlay and "text" in base.lower():
                base = base.replace("[TEXT]", text_overlay)
        if reference_image and "Midjourney" in platform:
            base += " --iw 2.0"
        return base

    async def generate_image_dalle(self, prompt: str, size="1024x1024"):
        if not settings.OPENAI_API_KEY:
            return {"error": "OPENAI_API_KEY no configurada"}
        headers = {"Authorization": f"Bearer {settings.OPENAI_API_KEY}", "Content-Type": "application/json"}
        payload = {"model": "dall-e-3", "prompt": prompt, "n": 1, "size": size, "quality": "standard"}
        response = requests.post("https://api.openai.com/v1/images/generations", headers=headers, json=payload)
        if response.status_code == 200:
            return {"url": response.json()["data"][0]["url"]}
        return {"error": response.text}