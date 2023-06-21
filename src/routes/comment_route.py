from fastapi import APIRouter

from models import CommentResponse, CommentStatus
from services import CommentService
from typing import Optional, Union

comment_router = APIRouter(prefix="/comment", tags=["Comment"])


@comment_router.get("/", response_model=list[CommentResponse])
def get_all_comments():
    all_post = CommentService().get_all()
    return all_post


@comment_router.get("/search", response_model=list[CommentResponse])
def search_comment(user_input: str):
    found_comment = CommentService().search_2(user_input)
    return found_comment


@comment_router.get("/search_using_celery")
def search_comment(user_input: str):
    found_comment = CommentService().search_3(user_input)
    return found_comment


@comment_router.get("/get_task", response_model=Union[list[CommentResponse],CommentStatus])
def get_task(task_id: str):
    found_task = CommentService().get_task(task_id)
    return found_task


@comment_router.get("/{post_id}", response_model=CommentResponse)
def get_comment_by_id(comment_id: int):
    selected_post = CommentService().get_by_id(comment_id)
    return selected_post
