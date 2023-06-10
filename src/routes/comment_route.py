from fastapi import APIRouter

from models import CommentResponse
from services import CommentService

comment_router = APIRouter(prefix="/comment", tags=["Comment"])

@comment_router.get("/", response_model=list[CommentResponse])
def get_all_post():
    all_post = CommentService().get_all() 
    return all_post

@comment_router.get("/search",response_model=list[CommentResponse])
def search_comment(user_input: str):
    found_comment = CommentService().search_2(user_input)
    return found_comment


@comment_router.get("/{post_id}", response_model=CommentResponse)
def get_post_by_id(post_id:str):
    selected_post = CommentService().get_by_id(post_id)
    return selected_post