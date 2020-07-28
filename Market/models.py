from django.db import models
from django.contrib.auth.models import User
from User.models import User_user


# Create your models here.
class BBS_goods(models.Model):
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    photo1 = models.ImageField(upload_to="Market/")
    photo2 = models.ImageField(upload_to="Market/")
    photo3 = models.ImageField(upload_to="Market/")
    view_count = models.IntegerField()
    content = models.TextField()
    prices = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 一对多
    tel = models.CharField(max_length=64)
    time = models.CharField(max_length=64)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        ordering = ['?']

    def __str__(self):
        return self.title
