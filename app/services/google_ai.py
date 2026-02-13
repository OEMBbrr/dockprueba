import requests
from app.core.config import settings

class GoogleAIService:
    def __init__(self):
        self.api_key = settings.GOOGLE_AI_API_KEY
        self.model = settings.GOOGLE_AI_MODEL
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"

    def _call_gemini(self, prompt: str, temperature: float = 0.7) -> str | None:
        if not self.api_key:
            return None
        url = f"{self.base_url}/{self.model}:generateContent?key={self.api_key}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": temperature, "maxOutputTokens": 500, "topP": 0.95, "topK": 40}
        }
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            candidates = data.get("candidates", [])
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                if parts:
                    return parts[0].get("text", "").strip()
        except Exception as e:
            print(f"Gemini error: {e}")
        return None

    def generate_title_variants(self, topic: str, emotion: str, count: int = 3) -> list[str]:
        prompt = (
            f"Eres un experto en títulos virales de YouTube para el nicho automotriz técnico. "
            f"Genera {count} títulos atractivos para un video sobre '{topic}' "
            f"con la emoción principal '{emotion}'. Los títulos deben ser en español, "
            f"incluir especificaciones técnicas si es posible, y tener entre 50 y 70 caracteres. "
            f"No uses comillas ni numeración. Sepáralos por saltos de línea."
        )
        result = self._call_gemini(prompt)
        return [line.strip() for line in result.split("\n") if line.strip()] if result else []

    def generate_thumbnail_copy_variants(self, title: str, emotion: str, count: int = 3) -> list[str]:
        prompt = (
            f"Genera {count} opciones de texto corto (máx 4 palabras) para una miniatura de YouTube. "
            f"El video se titula '{title}' y la emoción principal es '{emotion}'. "
            f"Usa mayúsculas si es apropiado. Responde solo con las frases, una por línea."
        )
        result = self._call_gemini(prompt)
        return [line.strip() for line in result.split("\n") if line.strip()] if result else []