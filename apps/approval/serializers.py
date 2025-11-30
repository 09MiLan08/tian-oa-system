from rest_framework import serializers
from .models import ApprovalType, Approval
from apps.user.serializers import UserSerializer

class ApprovalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalType
        fields = ["id", "name", "desc"]

class ApprovalSerializer(serializers.ModelSerializer):
    # 关联字段展示名称
    applicant_name = serializers.CharField(source="applicant.username", read_only=True)
    approver_name = serializers.CharField(source="approver.username", read_only=True)
    approval_type_name = serializers.CharField(source="approval_type.name", read_only=True)

    class Meta:
        model = Approval
        fields = ["id", "title", "content", "approval_type", "approval_type_name",
                  "applicant", "applicant_name", "approver", "approver_name",
                  "status", "reject_remark","create_time"]