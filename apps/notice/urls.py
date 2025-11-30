from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import NoticeViewSet

router = DefaultRouter()
router.register("notices", NoticeViewSet)  # 公告接口

urlpatterns = [path("", include(router.urls))]