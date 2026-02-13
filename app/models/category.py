from sqlalchemy import String, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from .base import Base

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(500))
    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("categories.id"))
    niche_specialization: Mapped[Optional[dict]] = mapped_column(JSON)

    parent: Mapped[Optional["Category"]] = relationship(remote_side=[id])
    children: Mapped[List["Category"]] = relationship(back_populates="parent")
    viral_patterns: Mapped[List["ViralPattern"]] = relationship(back_populates="category")
    thumbnail_copies: Mapped[List["ThumbnailCopy"]] = relationship(back_populates="category")
    description_templates: Mapped[List["DescriptionTemplate"]] = relationship(back_populates="category")