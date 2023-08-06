
from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated

from post.services import PostService
from post.serializers import PostListSerializer

from config.common.decorator import (
    required_data,
    optional_data,
)
from config.common.exceptions import ValidationException


class PostListAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    @required_data('title', 'content')
    def post(self, request, rd):
        try:
            post = PostService.create_post(rd['title'], rd['content'], request.user.id)
        
        except ValueError as e:
            raise ValidationException(e.errors()[0]['msg'])
        
        except Exception as e:
            raise APIException(e)
        
        context = {
            'post': PostListSerializer(post).data,
        }
        return JsonResponse(data=context, status=status.HTTP_201_CREATED)