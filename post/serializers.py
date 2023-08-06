from rest_framework.serializers import ModelSerializer

from post.models import Post


class PostSerializer(ModelSerializer):
    
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'created_at',
            'updated_at',
            'account_id',
        )
