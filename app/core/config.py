from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    PROJECT_NAME: str = "OEMB Studio"
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    OPENAI_API_KEY: str | None = Field(None, env="OPENAI_API_KEY")
    REPLICATE_API_TOKEN: str | None = Field(None, env="REPLICATE_API_TOKEN")
    STABILITY_API_KEY: str | None = Field(None, env="STABILITY_API_KEY")
    DEFAULT_IMAGE_PLATFORM: str = "dalle"

    # Google Gemini
    GOOGLE_AI_API_KEY: str | None = Field(None, env="GOOGLE_AI_API_KEY")
    GOOGLE_AI_MODEL: str = Field("gemini-1.5-flash", env="GOOGLE_AI_MODEL")

    # YouTube
    YOUTUBE_API_KEY: str | None = Field(None, env="YOUTUBE_API_KEY")

    class Config:
        env_file = ".env"

settings = Settings()