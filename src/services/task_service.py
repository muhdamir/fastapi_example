
from repository import TaskRepository
from  models import TaskResponse
class TaskService:
    def __init__(self, task_repository:TaskRepository) -> None:
        self.task_repository =task_repository

    def get_all(self):
        all =  self.task_repository.get_all()
        all = [TaskResponse.from_orm(a) for a in all]
        print(all)
        print(all)
