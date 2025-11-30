from rest_framework import viewsets, permissions
from django.db import models  # 新增：用于Q查询
from rest_framework.decorators import action  # 新增：用于自定义接口
from rest_framework.response import Response  # 新增：用于返回响应
from .models import ApprovalType, Approval
from .serializers import ApprovalTypeSerializer, ApprovalSerializer
from utils.permissions import IsAdminUser

# 审批类型视图（增删改查）
class ApprovalTypeViewSet(viewsets.ModelViewSet):
    queryset = ApprovalType.objects.all()
    serializer_class = ApprovalTypeSerializer
    permission_classes = [IsAdminUser]

# 审批单视图（核心业务）
class ApprovalViewSet(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer
    permission_classes = [permissions.IsAuthenticated]

    # 自定义：获取当前用户的审批单
    def get_queryset(self):
        # 申请人只能看自己的审批单，审批人能看自己的审批任务
        user = self.request.user
        return Approval.objects.filter(models.Q(applicant=user) | models.Q(approver=user))

    # 新增：审批通过接口
    @action(detail=True, methods=['post'])
    def pass_approval(self, request, pk=None):
        approval = self.get_object()
        # 只有审批人能操作
        if request.user != approval.approver:
            return Response({"msg": "你不是该审批单的审批人"}, status=403)
        approval.status = 2  # 状态设为“已通过”
        approval.save()
        return Response({"msg": "审批通过成功"})

    # 新增：审批驳回接口（带备注）
    @action(detail=True, methods=['post'])
    def reject_approval(self, request, pk=None):
        approval = self.get_object()
        # 只有审批人能操作
        if request.user != approval.approver:
            return Response({"msg": "你不是该审批单的审批人"}, status=403)
        # 获取前端传入的驳回备注
        reject_remark = request.data.get("reject_remark", "")
        approval.status = 3  # 状态设为“已驳回”
        approval.reject_remark = reject_remark  # 保存备注
        approval.save()
        return Response({
            "msg": "审批驳回成功",
            "reject_remark": approval.reject_remark
        })