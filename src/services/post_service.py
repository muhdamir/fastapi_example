from repository import PostRepository, CommentRepository

# logic
class PostService:
    repository = PostRepository()
    
    def get_all(self):
        all_data = self.repository.get_all()
        all_data = all_data.to_dict("records")
        return all_data
    
    def get_by_id(self, id:int):
        selected_data = self.repository.get_by_id(id)
        selected_data = selected_data.to_dict("records")[0]
        return selected_data
    