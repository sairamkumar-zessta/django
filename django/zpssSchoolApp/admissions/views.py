from admissions.models import student
from django.shortcuts import render 
from admissions.forms import StudentModelForm
# Create your views here.
def homePage(request):
    return render(request,'index.html')

def addAmission(request):
    form=StudentModelForm
    studentform={"form":form}


    if request.method=="POST":
        form =StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homePage(request)
    return render(request,'admissions/add-admission.html',studentform);

def getAdmissionDetails(request):
    #get all records from the table
    result=student.objects.all();#select * from students.
    students={'allstudents':result}
    return render(request,'admissions/admission-report.html',students) 