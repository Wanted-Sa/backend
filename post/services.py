from django.db import transaction

from post.models import Post

from config.common.exceptions import (
    NotFoundException, 
    ForbiddenException,
)


class PostService:
    @transaction.atomic
    def create_post(title:str, content:str, account_id:int) -> Post:
        post = Post.objects.create(title=title, content=content, account_id=account_id)
        return post
    
    @transaction.atomic
    def update_post(post_id:int, title:str, content:str, account_id:int) -> Post:
        try:
            post = Post.objects.get(id=post_id)
            
            if post.account_id != account_id:
                raise ForbiddenException("You don't have permission")
        
        except Post.DoesNotExist:
            raise NotFoundException("Post not found.")
        
        post.title = title
        post.content = content
        post.save()
        return post
    
    @transaction.atomic
    def hard_delete_post(post_id:int, account_id:int) -> None:
        try:
            post = Post.objects.get(id=post_id)
            
            if post.account_id != account_id:
                raise ForbiddenException("You don't have permission")
            
        except Post.DoesNotExist:
            raise NotFoundException("Post not found.")
        
        post.delete()
        return None
    
    @transaction.atomic
    def soft_delete_post(post_id:int, account_id:int) -> Post:
        try:
            post = Post.objects.get(id=post_id)
            
            if post.account_id != account_id:
                raise ForbiddenException("You don't have permission")
            
        except Post.DoesNotExist:
            raise NotFoundException("Post not found.")
        
        post.is_deleted = True
        post.save()
        return post