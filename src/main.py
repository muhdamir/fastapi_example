from fastapi import FastAPI

from routes import comment_router, post_comment_router, post_router, task_route

app = FastAPI(title="Test API", description="This is endpoints for the test")


@app.get("/", tags=["Test"])
def ping():
    return "pong"


app.include_router(post_router)
app.include_router(comment_router)
app.include_router(post_comment_router)
app.include_router(task_route)
