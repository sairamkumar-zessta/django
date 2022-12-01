from django.db import models

# Create your models here.

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=1000)
    fathername=models.CharField(max_length=1000)
    classname=models.IntegerField()
    address=models.TextField()
    dateofbirth=models.DateField(null=True)

from django.conf import settings 
from django.db.models.signals import post_save
from django.dispatch import receiver 
from rest_framework.authtoken.models import Token 

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
