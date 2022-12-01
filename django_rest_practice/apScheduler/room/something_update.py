
from django.conf import settings
from .models import Category
import random


#This creates one radom category-num object rin every 10 seconds
def create_object():
    print("this function runs every 10 seconds")
    number = random.randint(0,100)
    Category.objects.create(category_name = 'category-{}'.format(number))