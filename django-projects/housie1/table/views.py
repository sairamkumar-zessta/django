from django.shortcuts import render

# Create your views here.
def display_host(request):
    list_a =list(range(1,11))
    return render(request,'host.html',{'num':list_a})