from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.


def addAmission(request):
    return HttpResponse("<h1> This is add admission section you can enroll here </h1>")

def getAdmissionDetails(request):
    return HttpResponse("<h1> This is get admission details section you can get admission details here </h1>")
    