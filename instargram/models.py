from django.conf import settings
from django.db import models


class Post(models.Model):
    content = models.TextField()  # 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터를 추가한 시간
    updated_at = models.DateTimeField(auto_now=True)  # 현재 시간