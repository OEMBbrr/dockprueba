from sqlalchemy import String, Integer, Float, JSON
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from .base import Base

class ColorScheme(Base):
    __tablename__ = "color_schemes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    primary_color: Mapped[str] = mapped_column(String(30))
    secondary_color: Mapped[Optional[str]] = mapped_column(String(30))
    emotion: Mapped[Optional[str]] = mapped_column(String(100))
    placement_priority: Mapped[Optional[str]] = mapped_column(String(50))
    performance_boost: Mapped[Optional[float]]