from typing import Optional

import httpx
from fastapi import FastAPI

from models.post import PostResponse
from routes import post_router, comment_router, post_comment_router

app = FastAPI(
    title="Test API",
    description="This is endpoints for the test"
)

@app.get("/")
def ping():
    return "pong"

app.include_router(post_router)
app.include_router(comment_router)
app.include_router(post_comment_router)


"""
@app.get("/top_post", response_model=list[PostResponse])
def get_top_post():
    posts = httpx.get("https://jsonplaceholder.typicode.com/posts").json()
    comments = httpx.get("https://jsonplaceholder.typicode.com/comments").json()
    total_comment = {}
    for comment in comments:
        if comment["postId"] in total_comment:
            total_comment[comment["postId"]] = total_comment[comment["postId"]] + 1
        else:
            total_comment[comment["postId"]] = 1
    for post in posts:
        post["total_number_of_comments"] = total_comment[post["id"]]

    posts = sorted(posts, key=lambda d: d["total_number_of_comments"])
    return posts

@app.get("/comments", response_model=list[PostResponse])
def get_comments(post_id: Optional[int], post_title: Optional[str], post_body: Optional[str], total_number_of_comments: Optional[int]):
    all_post = get_top_post()
    all_post = list[PostResponse.pa](all_post)
    print(all_post)
    all_post = [PostResponse(**post).dict() for post in all_post]
    if post_id:
        all_post = list(filter(lambda x: x["post_id"] == post_id, all_post))
    if post_title:
        ...
    return all_post
"""
