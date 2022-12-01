from django.urls import path
from admissions.views import addAmission
from admissions.views import getAdmissionDetails

urlpatterns = [
    path('add/', addAmission),
    path('get/', getAdmissionDetails),
]