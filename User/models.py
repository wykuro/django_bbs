from django.db import models
from django.contrib.auth.models import User


class User_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 一对一
    number = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    dept = models.CharField(max_length=25)
    classs = models.CharField(max_length=25)
    tel = models.CharField(max_length=25)
    password = models.CharField(max_length=32, default="null")

    def __str__(self):
        return self.user.username
