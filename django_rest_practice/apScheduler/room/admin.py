from django.contrib import admin
from .models import Category
# Register your models here.
@admin.register(Category)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','category_name']