from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from .base import Base

class PowerVerb(Base):
    __tablename__ = "power_verbs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    verb: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    intensity: Mapped[int] = mapped_column(Integer, default=5)
    category: Mapped[Optional[str]] = mapped_column(String(50))