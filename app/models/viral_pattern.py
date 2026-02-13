from sqlalchemy import String, Integer, Float, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from .base import Base

class ViralPattern(Base):
    __tablename__ = "viral_patterns"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    pattern_template: Mapped[str] = mapped_column(String(500), nullable=False)
    psychological_triggers: Mapped[Optional[dict]] = mapped_column(JSON)  # lista de triggers
    ctr_range_min: Mapped[Optional[float]]
    ctr_range_max: Mapped[Optional[float]]
    avg_multiplier: Mapped[Optional[float]]
    success_rate: Mapped[Optional[float]]
    mining_evidence: Mapped[Optional[str]] = mapped_column(String(1000))
    best_for: Mapped[Optional[str]] = mapped_column(String(500))

    category: Mapped["Category"] = relationship(back_populates="viral_patterns")
    examples: Mapped[List["TitleExample"]] = relationship(back_populates="viral_pattern")