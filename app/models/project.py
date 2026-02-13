from sqlalchemy import String, Integer, JSON, ForeignKey, Enum, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
import enum
from datetime import datetime
from .base import Base

class ProjectStatus(str, enum.Enum):
    DRAFT = "draft"
    TITLE_SELECTED = "title_selected"
    THUMBNAIL_SELECTED = "thumbnail_selected"
    IMAGE_GENERATED = "image_generated"
    SEO_GENERATED = "seo_generated"
    COMPLETED = "completed"

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[str] = mapped_column(String(100))
    topic: Mapped[str] = mapped_column(String(500))
    emotion: Mapped[Optional[str]] = mapped_column(String(100))
    technical_level: Mapped[Optional[str]] = mapped_column(String(20))
    status: Mapped[ProjectStatus] = mapped_column(Enum(ProjectStatus), default=ProjectStatus.DRAFT)
    selected_title_id: Mapped[Optional[int]] = mapped_column(ForeignKey("title_examples.id"))
    selected_thumbnail_copy_id: Mapped[Optional[int]] = mapped_column(ForeignKey("thumbnail_copies.id"))
    image_prompt: Mapped[Optional[str]] = mapped_column(String(2000))
    generated_description: Mapped[Optional[str]] = mapped_column(String(5000))
    tags: Mapped[Optional[dict]] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    selected_title: Mapped[Optional["TitleExample"]] = relationship()
    selected_thumbnail_copy: Mapped[Optional["ThumbnailCopy"]] = relationship()