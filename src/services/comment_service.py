from repository import CommentRepository


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
        selected_data = self.repository.get_all()
        # searching process
        condition_1 = (
            selected_data["email"]
            .str.lower()
            .str.contains(str_input := user_input.lower() if user_input else "")
        )
        condition_2 = selected_data["name"].str.lower().str.contains(str_input)
        condition_3 = selected_data["body"].str.lower().str.contains(str_input)
        condition_4, condition_5 = False, False
        condition_4 = (
            (selected_data["postId"] == int(user_input))
            if user_input.isnumeric()
            else False
        )
        condition_5 = (
            (selected_data["id"] == int(user_input))
            if user_input.isnumeric()
            else False
        )
        condition = condition_1 | condition_2 | condition_3 | condition_4 | condition_5
        selected_data = selected_data.loc[condition, :]
        return selected_data.to_dict("records")
