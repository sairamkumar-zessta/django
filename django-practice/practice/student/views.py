from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def student_portal(request):
    return HttpResponse('<h3> This is Student Portal</h3>') 

def homePage(request):
    return HttpResponse('<h1> Hi this is Sai Ram Kumar Alladi Let\'s Learn Django Together </h1>')