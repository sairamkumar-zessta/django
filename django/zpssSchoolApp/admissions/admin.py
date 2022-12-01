from django.contrib import admin
from admissions.models import student
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','fathername','classname','address']
# Register your models here.
admin.site.register(student,StudentAdmin)