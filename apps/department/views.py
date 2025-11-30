from rest_framework import viewsets, permissions
from .models import Department, UserDepartment
from .serializers import DepartmentSerializer, UserDepartmentSerializer
from utils.permissions import IsAdminUser  # 复用管理员权限

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # 只有管理员能操作部门
    permission_classes = [IsAdminUser]

class UserDepartmentViewSet(viewsets.ModelViewSet):
    queryset = UserDepartment.objects.all()
    serializer_class = UserDepartmentSerializer
    # 只有管理员能关联用户和部门
    permission_classes = [IsAdminUser]