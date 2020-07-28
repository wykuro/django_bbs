from django.db import models
from django.contrib.auth.models import User
from User.models import User_user


class BBS_problems(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 一对多
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        ordering = ['?']

    def __int__(self):
        return self.id


class BBS_comments_problems(models.Model):
    comment = models.TextField()
    flag = models.ForeignKey(BBS_problems, on_delete=models.CASCADE)  # 一对多
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 一对多
    view_count = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.comment
