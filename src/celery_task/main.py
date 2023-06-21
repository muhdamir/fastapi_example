import json

import pandas as pd
from celery import Celery

from config import (
    RABBITMQ_DEFAULT_PASS,
    RABBITMQ_DEFAULT_USER,
    RABBITMQ_HOST,
    RABBITMQ_PORT,
)

celery_app = Celery(
    main="celery_task",
    broker=f"amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@{RABBITMQ_HOST}:{RABBITMQ_PORT}//",
    backend="rpc://",
)


@celery_app.task
def search(data: str, user_input: str) -> str:
    data: pd.DataFrame = pd.read_json(data)
    condition1 = (
        data["email"]
        .str.lower()
        .str.contains(string := (user_input.lower().strip() if user_input else ""))
    )
    condition2 = data["name"].str.lower().str.contains(string)
    condition3 = data["body"].str.lower().str.contains(string)
    condition4 = (data["postId"] == int(string)) if string.isnumeric() else False
    condition5 = (data["id"] == int(string)) if string.isnumeric() else False
    condition = condition1 | condition2 | condition3 | condition4 | condition5
    selected_data = data.loc[condition, :]
    result = json.dumps(selected_data.to_dict("records"))
    return result
