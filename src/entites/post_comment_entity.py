import pandas as pd

from error_messages import DataNotFound

from .comment_entity import CommentEntity
from .post_entity import PostEntity


class PostCommentEntity:

    def data(self):
        try:
            post_data = PostEntity().data().rename(columns={"id":"postId"})
            comment_data = CommentEntity().data()
            merged_data = post_data\
                .merge(comment_data,on="postId", how="right", suffixes=[None,"_y"])\
                .groupby(["postId","title","body"])\
                .agg(total_number_of_comments=("id","count"))\
                .reset_index()
            return merged_data
        
        except Exception:
            raise DataNotFound
        