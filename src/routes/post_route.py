from fastapi import APIRouter
from services import PostService
from models import PostResponse

post_router = APIRouter(prefix="/post", tags=["Post"])

@post_router.get("/", response_model=list[PostResponse])
def get_all_post():
    all_post = PostService().get_all() 
    return all_post

@post_router.get("/{post_id}", response_model=PostResponse)
def get_post_by_id(post_id:int):
    selected_post = PostService().get_by_id(post_id)
    return selected_post