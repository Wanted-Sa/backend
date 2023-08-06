from django.urls import path

from post.views import(
    PostListAPI,
    PostDetailAPI,
)


urlpatterns = [
    path('', PostListAPI.as_view(), name='post_list_view'),
    path('<int:post_id>', PostDetailAPI.as_view(), name='post_detail_view'),
]