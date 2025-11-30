from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import DepartmentViewSet, UserDepartmentViewSet

router = DefaultRouter()
router.register("departments", DepartmentViewSet)  # 部门接口
router.register("user-departments", UserDepartmentViewSet)  # 用户-部门关联接口

urlpatterns = [path("", include(router.urls))]