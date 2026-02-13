from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from .base import Base

class ProductionWorkflow(Base):
    __tablename__ = "production_workflows"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(500))
    steps: Mapped[dict] = mapped_column(JSON, nullable=False)