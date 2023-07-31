from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class ByteA:
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, bytes):
            raise ValueError(f'`bytes` expected not {type(v)}')
        return v.fromhex()

class TaskResponse(BaseModel):
    id:Optional[int]
    task_id:Optional[str]
    status:Optional[str]
    # result:ByteA
    date_done: Optional[datetime]
    traceback: Optional[str]
    name: Optional[str]
    args: Optional[str]
    kwargs: Optional[str]
    worker: Optional[str]
    retries: Optional[int]
    queue: Optional[str]

    class Config:
        orm_mode = True