from django.db import transaction

from post.models import Post

from config.common.exceptions import NotFoundException

class PostService:
    @transaction.atomic
    def create_post(title:str, content:str, account_id:int) -> Post:
        post = Post.objects.create(title=title, content=content, account_id=account_id)
        return post
    
    @transaction.atomic
    def update_post(post_id:int, title:str, content:str, account_id:int) -> Post:
        try:
            post = Post.objects.get(id=post_id, account_id=account_id)
            
        except Post.DoesNotExist:
            raise NotFoundException("Post not found.")
        
        post.title = title
        post.content = content
        post.save()
        return post