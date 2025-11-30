from rest_framework import permissions

# 自定义权限：只有管理员才能访问
class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # 验证用户是否登录，且角色为管理员（role=1）
        return request.user.is_authenticated and request.user.role == 0