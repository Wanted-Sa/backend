from django.db import transaction

from post.models import Post


class PostService:
    @transaction.atomic
    def create_post(title:str, content:str, account_id:int) -> Post:
        post = Post.objects.create(title=title, content=content, account_id=account_id)
        return post
    