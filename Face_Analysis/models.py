from django.db import models

# Create your models here.
class f_change_data(models.Model):
    lefteyex= models.CharField(max_length=100)
    lefteyey = models.CharField(max_length=100)
    rihgteyex = models.CharField(max_length=100)
    rihgteyey = models.CharField(max_length=100)
    rotation = models.CharField(max_length=100)
    distance = models.CharField(max_length=100)
    ratio = models.CharField(max_length=100)

