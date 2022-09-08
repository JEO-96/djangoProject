from django.conf import settings
from django.db import models


class Post(models.Model):
    message = models.TextField()  # 내용.
    photo = models.ImageField(blank=True, upload_to='instargram/post/%Y/%m/%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터를 추가한 시간
    updated_at = models.DateTimeField(auto_now=True)  # 현재 시간

    def __str__(self):
        return self.message

