from django.db import models

class User(models.Model):
    wechat_name = models.CharField(max_length=50)
    mobile = models.CharField(unique=True, max_length=11)
    openid = models.CharField(unique=True,max_length=100)
    wechat_photo = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

