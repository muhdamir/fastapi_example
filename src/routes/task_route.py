from fastapi import APIRouter, Depends
from services import TaskService
from infrastructure.postgres import get_session
from sqlalchemy.orm import Session
from repository import TaskRepository
from models import TaskResponse
from typing import Optional


task_route = APIRouter(prefix="/task", tags=["Task"])

def gen_taskservice(session: Session = Depends(get_session)):
    # repository depends on session
    task_repository = TaskRepository(session)
    # service depends on service
    task_service = TaskService(task_repository)
    return task_service




@task_route.get("/", response_model=list[Optional[TaskResponse]])
async def get_task(task_service:TaskService = Depends(gen_taskservice)):
    all_task = task_service.get_all()
    return all_task