from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="백엔드 프리온보딩 인터십 사전과제 ",
        default_version="v1",
        description="백엔드 프리온보딩 인터십 사전과제 API 문서입니다.",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        license=openapi.License(name="Wanted Task License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API
    path('api/v1/account/', include('account.urls')),
    path('api/v1/post/', include('post.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)