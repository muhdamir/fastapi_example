import pandas as pd

from repository import CommentRepository
from celery_task.main import search, celery_app
from celery.result import AsyncResult
import json


# logic
class CommentService:
    repository = CommentRepository()

    def get_all(self):
        all_data = self.repository.get_all()
        all_data = all_data.to_dict("records")
        return all_data

    def get_by_id(self, id: int):
        selected_data = self.repository.get_by_id(id)
        selected_data = selected_data.to_dict("records")[0]
        return selected_data

    def search_2(self, user_input: str):
        data = self.repository.get_all()
        # searching process
        condition_1 = self.Utils.search_str(data, "email", user_input)
        condition_2 = self.Utils.search_str(data, "name", user_input)
        condition_3 = self.Utils.search_str(data, "body", user_input)
        condition_4, condition_5 = False, False
        condition_4 = self.Utils.search_int(data, "postId", user_input)
        condition_5 = self.Utils.search_int(data, "id", user_input)
        condition = condition_1 | condition_2 | condition_3 | condition_4 | condition_5
        selected_data = data.loc[condition, :]
        return selected_data.to_dict("records")

    def search_3(self, user_input: str):
        data = self.repository.get_all().to_json()
        job = search.delay(data, user_input)
        return job.id

    def get_task(self, id: str):
        res = AsyncResult(id, app=celery_app)
        if res.state == "SUCCESS":
            return json.loads(res.get())
        return {"job_id": id, "status": res.state}

    # TODO: take Utils as module
    #  for now class Utils is declared here for easy access
    class Utils:
        @classmethod
        def search_str(
            cls,
            data: pd.DataFrame,
            col: str,
            string: str,
        ):
            condition = (
                data[col].str.lower().str.contains(string.lower() if string else "")
            )
            return condition

        @classmethod
        def search_int(
            cls,
            data: pd.DataFrame,
            col: str,
            int_str: str,
        ):
            condition = (data[col] == int(int_str)) if int_str.isnumeric() else False
            return condition
