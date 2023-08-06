from django.urls import path
from account.views import (
    SingUpAPI,
)

urlpatterns = [
    path('signup', SingUpAPI.as_view(), name='signup'),
]
