from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    title=models.TextField(null=True , blank = True)
    status=models.CharField(default=  'inactive', max_length=100) 
    created_by=models.ForeignKey(User, null=True, blank=True , on_delete=models.CASCADE) 

    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self) :
        return self.title