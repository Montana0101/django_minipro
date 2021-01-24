from django.db import models

class User(models.Model):
    wechat_name = models.CharField(max_length=50,null=True)
    mobile = models.CharField(unique=False, max_length=11,null=True)
    openid = models.CharField(unique=True,max_length=100)
    wechat_photo = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    gender = models.IntegerField(null=True)
    province = models.CharField(max_length=50,null=True)
    city = models.CharField(null=True, max_length=50)
    area = models.CharField(max_length=50,null=True)
    pass


