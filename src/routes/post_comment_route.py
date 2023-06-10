from fastapi import APIRouter

from models import PostCommentResponse
from services import PostCommentService

post_comment_router = APIRouter(
    prefix="/post_with_comments", tags=["Post with comment count"]
)


@post_comment_router.get("/", response_model=list[PostCommentResponse])
def get_all_post():
    all_post = PostCommentService().get_all()
    return all_post


@post_comment_router.get("/top_post")
def get_top_post():
    sorted_post = PostCommentService().get_sorted()
    return sorted_post


@post_comment_router.get("/{post_id}", response_model=PostCommentResponse)
def get_post_by_id(post_id: int):
    selected_post = PostCommentService().get_by_id(post_id)
    return selected_post
