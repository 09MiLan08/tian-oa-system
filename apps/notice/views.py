from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Notice
from .serializers import NoticeSerializer
from utils.permissions import IsAdminUser

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    def get_permissions(self):
        if self.action in["create","publish","take_down"]:
            return[IsAdminUser()]
        return [permissions.IsAuthenticated()]

    # 自定义：发布公告（修改状态为“已发布”）
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        notice = self.get_object()
        notice.status = 1  # 状态设为“已发布”
        notice.save()
        return Response({"msg": "公告发布成功"})

    # 自定义：下架公告（修改状态为“已下架”）
    @action(detail=True, methods=['post'])
    def take_down(self, request, pk=None):
        notice = self.get_object()
        notice.status = 2  # 状态设为“已下架”
        notice.save()
        return Response({"msg": "公告下架成功"})