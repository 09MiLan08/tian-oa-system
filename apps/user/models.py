from django.db import models
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='企业名称')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='地址')
    industry = models.CharField(max_length=50, null=True, blank=True, verbose_name='行业')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'tb_company'
        verbose_name = '企业'
        verbose_name_plural = '企业'

class User(AbstractUser):

    ROLE_CHOICES = (  
    (1,"普通用户"),
    (0,"管理员"),
    )

    

    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属企业')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    position = models.CharField(max_length=50, null=True, blank=True, verbose_name='职位')
    role = models.IntegerField(choices=ROLE_CHOICES, default=0, verbose_name="用户角色")  
    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户'
        verbose_name_plural = '用户'