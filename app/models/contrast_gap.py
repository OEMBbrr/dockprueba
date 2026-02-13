from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class ContrastGap(Base):
    __tablename__ = "contrast_gaps"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    gap_text: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)