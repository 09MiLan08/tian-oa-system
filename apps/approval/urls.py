from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ApprovalTypeViewSet, ApprovalViewSet

router = DefaultRouter()
router.register("types", ApprovalTypeViewSet)  # 审批类型接口
router.register("approvals", ApprovalViewSet)   # 审批单接口

urlpatterns = [path("", include(router.urls))]