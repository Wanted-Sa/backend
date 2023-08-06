from django.urls import path
from account.views import (
    SignUpAPI,
    SignInAPI,
)

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup', SignUpAPI.as_view(), name='signup_view'),
    path('signin', SignInAPI.as_view(), name='signin_view'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh_view'),
]
