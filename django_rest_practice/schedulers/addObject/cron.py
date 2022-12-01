from django.conf import settings
from .models import Category
import random



def create_category():
    number = random.randint(0,100)
    Category.objects.create(Category_name = 'category-{}'.format(number))