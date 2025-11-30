from rest_framework import serializers
from .models import Department, UserDepartment
from apps.user.serializers import UserSerializer

class DepartmentSerializer(serializers.ModelSerializer):
    leader_name = serializers.CharField(source="leader.username", read_only=True)
    children = serializers.SerializerMethodField()  # 嵌套子部门

    def get_children(self, obj):
        return DepartmentSerializer(obj.children.all(), many=True).data

    class Meta:
        model = Department
        fields = ["id", "name", "parent", "leader", "leader_name", "desc", "children", "create_time"]

class UserDepartmentSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source="user", read_only=True)
    department_info = DepartmentSerializer(source="department", read_only=True)

    class Meta:
        model = UserDepartment
        fields = ["id", "user", "user_info", "department", "department_info"]