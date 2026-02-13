from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from .base import Base

class Archetype(Base):
    __tablename__ = "archetypes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    emotional_trigger: Mapped[Optional[str]] = mapped_column(String(200))
    syntax_template: Mapped[Optional[str]] = mapped_column(String(500))
    power_verbs: Mapped[Optional[dict]] = mapped_column(JSON)
    amplifiers: Mapped[Optional[dict]] = mapped_column(JSON)