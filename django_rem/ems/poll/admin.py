from django.contrib import admin
from .models import Question
# Register your models here.
@admin.register(Question) 
class pollAdmin(admin.ModelAdmin):
    list_display = ['title','status','created_by','created_at','updated_at']
