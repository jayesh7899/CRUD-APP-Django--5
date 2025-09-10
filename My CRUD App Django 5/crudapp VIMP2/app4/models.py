from django.db import models

# Create your models here.

class Datas(models.Model):
    name=models.CharField(max_length=40, default="")
    age=models.IntegerField(default="")
    address=models.CharField(max_length=40,default="")
    contact=models.IntegerField(default="")
    mail=models.CharField(max_length=50, default="")