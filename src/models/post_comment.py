from pydantic import BaseModel, Field


class PostCommentResponse(BaseModel):
    postId: int = Field(alias="post_id")
    title: str = Field(alias="post_title")
    body: str = Field(alias="post_body")
    total_number_of_comments: int

    class Config:
        allow_population_by_field_name = True
