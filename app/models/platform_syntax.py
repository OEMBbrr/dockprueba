from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from .base import Base

class PlatformSyntax(Base):
    __tablename__ = "platform_syntax"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    platform_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    syntax_template: Mapped[str] = mapped_column(String(1000))
    forbidden_words: Mapped[Optional[dict]] = mapped_column(JSON)
    notes: Mapped[Optional[str]] = mapped_column(String(500))