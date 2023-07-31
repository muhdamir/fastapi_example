
from entites import TaskEntity
from sqlalchemy.orm import Session

class TaskRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self):
        all = self.session.query(TaskEntity).all()
        return all
