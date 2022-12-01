from django.shortcuts import render
from admissions.models import Student 
from admissions.forms import StudentModelForm
from admissions.forms import VendorForm
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.
def homePage(request):
    return render(request,'index.html')
@login_required
@permission_required('admissions.add_student')
def addAdmission(request):
    form=StudentModelForm
    studentform={"form":form}
    if request.method=="POST":
        form =StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homePage(request)
    return render(request,'admissions/add_admission.html',studentform);
@login_required
def admissionReport(request):
    res=Student.objects.filter(dateofbirth__year__gte=2002) & Student.objects.filter(dateofbirth__year__lte=2005)#select * from student
    student_details={"allstudents":res}

    return render(request,'admissions/admission_rep.html',student_details)
def addVendor(request):
    form=VendorForm
    vform={"form":form}


    if request.method=="POST":
        form =VendorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['address'])
            print(form.cleaned_data['contactdetails'])
            print(form.cleaned_data['item'])
        return homePage(request)
    return render(request,'admissions/add_vendor.html',vform);