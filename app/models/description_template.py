from sqlalchemy import String, JSON, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from .base import Base

class DescriptionTemplate(Base):
    __tablename__ = "description_templates"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    name: Mapped[str] = mapped_column(String(100))
    template_text: Mapped[str] = mapped_column(String(5000))
    retention_boost: Mapped[Optional[float]]
    sections: Mapped[Optional[dict]] = mapped_column(JSON)

    category: Mapped["Category"] = relationship(back_populates="description_templates")