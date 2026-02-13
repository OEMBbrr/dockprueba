from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.orchestrator.workflow import WorkflowOrchestrator
from app.models import ProductionWorkflow, WorkflowInstance, Project
from pydantic import BaseModel

router = APIRouter()

class WorkflowStartRequest(BaseModel):
    project_id: int
    workflow_id: int | None = None

class StepInput(BaseModel):
    instance_id: int
    step_id: str
    inputs: dict

@router.post("/start")
def start_workflow(req: WorkflowStartRequest, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == req.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    workflow_id = req.workflow_id or 1
    workflow = db.query(ProductionWorkflow).filter(ProductionWorkflow.id == workflow_id).first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Flujo no encontrado")

    instance = WorkflowInstance(
        workflow_id=workflow.id,
        status="active",
        current_step_id=workflow.steps[0]["id"],
        data={"project_id": project.id}
    )
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return {"instance_id": instance.id, "current_step": instance.current_step_id}

@router.post("/step")
def execute_step(inputs: StepInput, db: Session = Depends(get_db)):
    instance = db.query(WorkflowInstance).filter(WorkflowInstance.id == inputs.instance_id).first()
    if not instance:
        raise HTTPException(status_code=404, detail="Instancia no encontrada")
    orchestrator = WorkflowOrchestrator(db)
    next_step = orchestrator.process_step(instance, inputs.step_id, inputs.inputs)
    return {"instance_id": instance.id, "next_step": next_step}