from sqlalchemy import String, Integer, JSON, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
import enum
from .base import Base

class WorkflowStatus(str, enum.Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"

class WorkflowInstance(Base):
    __tablename__ = "workflow_instances"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    workflow_id: Mapped[int] = mapped_column(ForeignKey("production_workflows.id"))
    status: Mapped[WorkflowStatus] = mapped_column(Enum(WorkflowStatus), default=WorkflowStatus.PENDING)
    current_step_id: Mapped[Optional[str]] = mapped_column(String(50))
    data: Mapped[Optional[dict]] = mapped_column(JSON)

    workflow: Mapped["ProductionWorkflow"] = relationship()