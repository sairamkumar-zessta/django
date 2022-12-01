from django.urls import path 
from admissions.views import addAdmission
from admissions.views import admissionReport
from admissions.views import addVendor
urlpatterns=[
    path('add/', addAdmission),
    path('getrep/', admissionReport),
    path('vendor/', addVendor),
]
