from pydantic import BaseModel, Field

class PostResponse(BaseModel):
    id: int = Field(alias="post_id")
    title: str = Field(alias="post_title")
    body: str = Field(alias="post_body")

    class Config:
        allow_population_by_field_name = True
