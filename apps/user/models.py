from django.db import models
from django.contrib.auth.models import AbstractUser

# 企业表：记录企业信息
class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name="企业名称")  # 企业名称（必填）
    address = models.CharField(max_length=255, blank=True, verbose_name="企业地址")  # 地址（选填）
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")  # 自动记录创建时间

    class Meta:
        verbose_name = "企业"
        verbose_name_plural = "企业"  # 后台显示的复数名称

    def __str__(self):
        return self.name  # 后台显示企业名称，而非对象ID


# 用户表：继承Django内置User，扩展“所属企业”“手机号”字段
class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="users", verbose_name="所属企业",null=True,blank=True)  # 关联企业
    phone = models.CharField(max_length=11, blank=True, verbose_name="手机号")  # 手机号（选填）

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"