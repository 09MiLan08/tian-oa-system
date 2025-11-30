from django.db import models
from apps.user.models import User  # 关联用户模块的User模型

# 审批类型（比如请假、报销）
class ApprovalType(models.Model):
    name = models.CharField(max_length=50, verbose_name="审批类型名称")
    desc = models.CharField(max_length=200, null=True, blank=True, verbose_name="类型描述")
    reject_remark = models.TextField(null=True, blank=True, verbose_name="驳回备注")  

    class Meta:
        db_table = "tb_approval_type"
        verbose_name = "审批类型"
        verbose_name_plural = "审批类型"

# 审批单（核心模型）
class Approval(models.Model):
    # 审批状态：草稿/待审批/已通过/已驳回
    STATUS_CHOICES = (
        (0, "草稿"),
        (1, "待审批"),
        (2, "已通过"),
        (3, "已驳回"),
    )
    title = models.CharField(max_length=100, verbose_name="审批单标题")
    content = models.TextField(verbose_name="审批内容")
    approval_type = models.ForeignKey(ApprovalType, on_delete=models.CASCADE, verbose_name="审批类型")
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_approvals", verbose_name="申请人")
    approver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="approve_tasks", verbose_name="审批人")
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name="审批状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "tb_approval"
        verbose_name = "审批单"
        verbose_name_plural = "审批单"