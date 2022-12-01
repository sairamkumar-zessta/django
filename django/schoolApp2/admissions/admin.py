from django.contrib import admin

# Register your models here.
from .models import Student 

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','fathername','classname','address','dateofbirth']

admin.site.register(Student,StudentAdmin)