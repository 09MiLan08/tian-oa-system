from django.contrib import admin
from .models import ApprovalType, Approval

admin.site.register(ApprovalType)
admin.site.register(Approval)