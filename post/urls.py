from django.urls import path

from post.views import(
    PostListAPI,
)


urlpatterns = [
    path('', PostListAPI.as_view(), name='post_list_view'),
]