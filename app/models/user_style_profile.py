from sqlalchemy import String, JSON, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime
from .base import Base

class UserStyleProfile(Base):
    __tablename__ = "user_style_profiles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[str] = mapped_column(String(100), unique=True)
    script_samples: Mapped[Optional[dict]] = mapped_column(JSON)
    tonal_signature: Mapped[Optional[str]] = mapped_column(String(100))
    common_phrases: Mapped[Optional[dict]] = mapped_column(JSON)
    technical_depth: Mapped[Optional[str]] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())