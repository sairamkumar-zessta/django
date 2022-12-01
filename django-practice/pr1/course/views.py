from django.shortcuts import render

# Create your views here.
def learn_django(request):
    c_name = 'Django'
    duration = '4months'
    seats = 40
    details = {'cn':c_name,'dur':duration,'st':seats}
    return render(request,'course/course1.html',context = details)
def learn_python(request):
    c_name = 'Python'
    duration = '3months'
    seats = 30
    details = {'cn':c_name,'dur':duration,'st':seats}
    return render(request,'course/course2.html',details)