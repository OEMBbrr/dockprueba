from sqlalchemy import String, Integer, Float, JSON, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from datetime import datetime
from .base import Base

class VideoAnalytics(Base):
    __tablename__ = "video_analytics"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    video_title: Mapped[str] = mapped_column(String(200))
    published_date: Mapped[datetime] = mapped_column(DateTime)
    views: Mapped[int]
    ctr: Mapped[float]
    retention: Mapped[Optional[float]]
    impressions: Mapped[Optional[int]]
    subscriber_gain: Mapped[Optional[int]]
    pattern_id_used: Mapped[Optional[int]] = mapped_column(ForeignKey("viral_patterns.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    pattern: Mapped[Optional["ViralPattern"]] = relationship()