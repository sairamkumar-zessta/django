from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def learn_django(request):
    return HttpResponse('Hello Django') 
def learn_python(request):
    return HttpResponse('<h1> Hello Python</h1>')
def learn_frontend(request):
    req = '<h1> Frontend Technologies </h1><ul> <li>HTML</li> <li>CSS</li> <li>Bootstrap</li> <li>Javascript</li></ul>'
    return HttpResponse(req)
def learn_math(request):
    a = 10 + 10
    return HttpResponse(a)
def greet(request):
    a = 'Sai Ram Kumar Alladi'
    return HttpResponse(f'Hello This is {a} welcome to coding world')

