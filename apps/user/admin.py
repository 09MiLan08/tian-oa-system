from django.contrib import admin
from .models import User, Company  # 导入你自定义的模型

# 注册User模型到Admin后台
admin.site.register(User)
# 注册Company模型到Admin后台
admin.site.register(Company)