from django.db import models
from apps.user.models import User

class Department(models.Model):
    """部门模型（支持层级结构，比如部门下的子部门）"""
    name = models.CharField(max_length=50, verbose_name="部门名称")
    parent = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="children",
        verbose_name="上级部门"
    )
    leader = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="部门负责人"
    )
    desc = models.CharField(max_length=200, null=True, blank=True, verbose_name="部门描述")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        db_table = "tb_department"
        verbose_name = "部门"
        verbose_name_plural = "部门"

# 关联用户和部门（多对多，一个用户可属于多个部门）
class UserDepartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="部门")

    class Meta:
        db_table = "tb_user_department"
        unique_together = ("user", "department")  # 避免重复关联