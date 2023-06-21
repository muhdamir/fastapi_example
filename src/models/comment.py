from pydantic import BaseModel, Field


class CommentResponse(BaseModel):
    postId: int = Field(alias="post_id")
    id: int = Field(alias="comment_id")
    body: str = Field(alias="comment_body")
    name: str
    email: str

    class Config:
        allow_population_by_field_name = True

class CommentStatus(BaseModel):
    job_id: str
    status: str
