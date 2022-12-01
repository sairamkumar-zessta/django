from django.contrib import admin
from .models import StudentModel
# Register your models here.
@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','class_name','date_of_birth','age']