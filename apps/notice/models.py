from django.db import models
from apps.user.models import User  # 关联用户模块

class Notice(models.Model):
    # 公告状态：草稿/已发布/已下架
    STATUS_CHOICES = (
        (0, "草稿"),
        (1, "已发布"),
        (2, "已下架"),
    )
    title = models.CharField(max_length=100, verbose_name="公告标题")
    content = models.TextField(verbose_name="公告内容")
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="发布人")
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name="公告状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "tb_notice"
        verbose_name = "公告"
        verbose_name_plural = "公告"
        ordering = ["-create_time"]  # 默认按创建时间倒序