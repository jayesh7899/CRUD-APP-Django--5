from django.db import models

# Create your models here.

class Student(models.Model):
    stud_id=models.CharField(max_length=80)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    contact=models.CharField(max_length=30)

    

