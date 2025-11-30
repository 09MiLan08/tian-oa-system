from rest_framework import serializers
from .models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    # 关联字段展示发布人姓名
    publisher_name = serializers.CharField(source="publisher.username", read_only=True)

    class Meta:
        model = Notice
        fields = ["id", "title", "content", "publisher", "publisher_name",
                  "status", "create_time", "update_time"]