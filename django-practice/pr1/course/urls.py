from operator import le

from course.views import *
from django.urls import path
urlpatterns = [
    path('django/', learn_django),
    path('python/', learn_python),
]