import pandas as pd

from entites import PostCommentEntity

from .base_repository_interface import BaseRepositoryInterface


class PostCommentRepository(BaseRepositoryInterface):
    entity = PostCommentEntity()

    def get_all(self) -> pd.DataFrame:
        df = self.entity.data()
        return df

    def get_by_id(self, id: int):
        df = self.entity.data()
        selected = df.query(f"postId == {id}")
        return selected

    def get_sorted(self):
        df = self.entity.data()
        # demo comment
        df.loc[2, "total_number_of_comments"] = 30
        df.loc[33, "total_number_of_comments"] = 55
        sorted = df.sort_values(
            by=["total_number_of_comments", "postId"], ascending=False
        )
        return sorted
