from sqlalchemy import String, JSON, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from .base import Base

class TitleExample(Base):
    __tablename__ = "title_examples"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    viral_pattern_id: Mapped[int] = mapped_column(ForeignKey("viral_patterns.id"))
    title_text: Mapped[str] = mapped_column(String(200), nullable=False)
    ctr_estimate: Mapped[Optional[float]]
    emotional_triggers: Mapped[Optional[dict]] = mapped_column(JSON)
    technical_specs: Mapped[Optional[dict]] = mapped_column(JSON)
    source_channel: Mapped[Optional[str]] = mapped_column(String(100))

    viral_pattern: Mapped["ViralPattern"] = relationship(back_populates="examples")