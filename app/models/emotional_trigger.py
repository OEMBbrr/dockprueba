from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class EmotionalTrigger(Base):
    __tablename__ = "emotional_triggers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    potency: Mapped[int] = mapped_column(Integer, default=50)