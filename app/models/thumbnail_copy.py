from sqlalchemy import String, Integer, Float, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
import enum
from .base import Base

class PlacementEnum(str, enum.Enum):
    TOP_LEFT = "Top-Left"
    TOP_RIGHT = "Top-Right"
    BOTTOM_LEFT = "Bottom-Left"
    BOTTOM_RIGHT = "Bottom-Right"
    CENTER = "Center"
    CENTER_TOP = "Center-Top"
    CENTER_BOTTOM = "Center-Bottom"

class ThumbnailCopy(Base):
    __tablename__ = "thumbnail_copies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    text: Mapped[str] = mapped_column(String(50), nullable=False)
    placement: Mapped[Optional[PlacementEnum]] = mapped_column(Enum(PlacementEnum))
    color_scheme: Mapped[Optional[str]] = mapped_column(String(50))
    readability_score: Mapped[Optional[float]]
    best_for: Mapped[Optional[str]] = mapped_column(String(500))

    category: Mapped["Category"] = relationship(back_populates="thumbnail_copies")