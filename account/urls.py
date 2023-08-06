from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from account.views import (
    SignUpAPI,
    SignInAPI,
)

urlpatterns = [
    path('signup', SignUpAPI.as_view(), name='signup_view'),
    path('signin', SignInAPI.as_view(), name='signin_view'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh_view'),
]
