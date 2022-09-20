from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()  # 내용.
    photo = models.ImageField(blank=True, upload_to='instargram/post/%Y/%m/%d')
    tag_set = models.ManyToManyField('Tag', blank=True)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터를 추가한 시간
    updated_at = models.DateTimeField(auto_now=True)  # 현재 시간

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             limit_choices_to={'is_public': True})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터를 추가한 시간
    updated_at = models.DateTimeField(auto_now=True)  # 현재 시간


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
