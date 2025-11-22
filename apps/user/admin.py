from django.contrib import admin
from .models import Company, User  # 导入刚才写的模型


# 注册企业模型到Admin
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "create_time")  # 列表页显示的字段
    search_fields = ("name",)  # 支持按企业名称搜索


# 注册用户模型到Admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "company", "phone", "is_active")  # 列表页显示的字段
    list_filter = ("company", "is_active")  # 支持按“企业”“是否激活”筛选
    search_fields = ("username", "company__name")  # 支持按用户名、企业名称搜索