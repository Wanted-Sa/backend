from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated

from post.services import PostService
from post.serializers import PostListSerializer
from post.selectors import PostSelector

from config.common.decorator import (
    required_data,
    optional_data,
)
from config.common.pagination import PaginationHandlerMixin, BasePagination
from config.common.exceptions import ValidationException


class PostListAPI(PaginationHandlerMixin, APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = BasePagination
    
    @required_data('title', 'content')
    def post(self, request, rd):
        try:
            post = PostService.create_post(rd['title'], rd['content'], request.user.id)
        
        except Exception as e:
            raise APIException(e)
        
        context = {
            'post': PostListSerializer(post).data,
        }
        return Response(data=context, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        try:
            post = PostSelector.get_post_all()
            post_page = self.paginate_queryset(post)
            
        except Exception as e:
            raise APIException(e)
        
        post_serializer = self.get_paginated_response(PostListSerializer(post_page, many=True).data)
        
        context = {
            'post': post_serializer.data
        }
        return Response(data=context, status=status.HTTP_200_OK)


# class PostDetailAPI(APIView):
#     permission_classes = [Is]
    
    