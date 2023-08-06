from abc import ABC, abstractmethod

from django.db.models.query import QuerySet

from post.models import Post

from config.common.exceptions import NotFoundException


class AbstractPostSelector(ABC):
    @abstractmethod
    def get_post_all(self) -> QuerySet[Post]:
        pass    
    
    @abstractmethod
    def get_post_by_id(self, post_id: int) -> QuerySet[Post]:
        pass
    
    
class PostSelector(AbstractPostSelector):
    def get_post_all() -> QuerySet[Post]:
        return Post.objects.all()

    def get_post_by_id(post_id: int) -> QuerySet[Post]:
        try:
            post = Post.objects.get(id=post_id)
            return post
        
        except Post.DoesNotExist:
            raise NotFoundException("Post not found.")