import pandas as pd

from entites import CommentEntity

from .base_repository_interface import BaseRepositoryInterface


class CommentRepository(BaseRepositoryInterface):
    entity = CommentEntity()

    def get_all(self) -> pd.DataFrame:
        df = self.entity.data()
        return df
    
    def get_by_id(self, id:int):
        df = self.entity.data(id)
        return df
        

