from django.db import models

# Create your models here.
class appoints(models.Model):
        name=models.CharField(max_length=100)
        phone=models.IntegerField()
        email=models.EmailField(max_length=100)
        address=models.CharField(max_length=100)
        schedule=models.CharField(max_length=100,default=0)
        day=models.CharField(max_length=100)
        message=models.CharField(max_length=100,default="")