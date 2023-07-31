from .base_orm import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Index, Integer, String, Text
from sqlalchemy.dialects.postgresql import BYTEA, TIMESTAMP, INT4MULTIRANGE


class TaskEntity(Base):
    __tablename__ = "celery_taskmeta"
    id = mapped_column(Integer, primary_key=True, nullable=False)
    task_id = mapped_column(String(155))
    status = mapped_column(String(50))
    result = mapped_column(BYTEA)
    date_done = mapped_column(TIMESTAMP)
    traceback = mapped_column(Text)
    name = mapped_column(String(155))
    args = mapped_column(BYTEA)
    kwargs = mapped_column(BYTEA)
    worker = mapped_column(String(155))
    retries = mapped_column(INT4MULTIRANGE)
    queue = mapped_column(String(155))
    __table_args__ = (
        Index("celery_taskmeta_pkey", id, unique=True),
        Index("celery_taskmeta_task_id_key", task_id, unique=True),
    )
