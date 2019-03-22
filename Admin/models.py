# encoding UTF-8
from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField,
    AGE_CHOICES = ((0, 'less_18'),(1,'18-35'),(2, 'older_35')),
    age_choice = AGE_CHOICES,

    SEX_CHOICES = ((0, 'male'), (1, 'female')),
    sex_choice = SEX_CHOICES ,

    CHARACTER_CHOICES = ((0, 'outgoing'), (1, 'eligent'),(2, 'mature'),(3,'citizen'))
    character_choice = CHARACTER_CHOICES,


    def __unicode__(self):
        return self


