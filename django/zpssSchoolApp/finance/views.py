from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.




def feeCollection(request):
    return HttpResponse("<h1>This is Fee collection section you can pay fee here</h1>")
def feeDueReport(request):
    return HttpResponse("<h1>This is Fee due report section you can check your due here</h1>")
def feeCollectedReport(request):
    return HttpResponse("<h1>This is Fee collected Report section you can check fee conformation here</h1>")




