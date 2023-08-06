from abc import ABC
from abc import abstractmethod

from django.db.models.query import QuerySet

from post.models import Post

class AbstractPostSelector(ABC):
    @abstractmethod
    def get_post_all(self) -> QuerySet[Post]:
        pass
    
    
class PostSelector(AbstractPostSelector):
    def get_post_all() -> QuerySet[Post]:
        return Post.objects.all()
