from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, CompanyViewSet  # 只导入ViewSet，不用导入login

router = DefaultRouter()
router.register('users', UserViewSet)  # 自动包含UserViewSet的所有action（包括login）
router.register('companies', CompanyViewSet)

# 直接包含router的路由，login接口会自动注册为/api/users/login/
urlpatterns = [
    path('', include(router.urls))
]