from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentModelForm
from .models import StudentModel
# Create your views here.


def studentView(request):
    if request.method == 'POST':
        req = StudentModelForm(request.POST)
        if req.is_valid():
            req.save()
            return HttpResponseRedirect('/')
    else:
        objs = StudentModel.objects.all()

        return render(request,'index.html',{'forms':StudentModelForm,'req':objs})

def delete_data(request,id):
    if request.method == 'POST':
        need = StudentModel.objects.get(pk = id)
        need.delete()
        return HttpResponseRedirect('/')
def update_data(request,id):
    if request.method == 'POST':
        need = StudentModel.objects.get(pk= id)
        req = StudentModelForm(request.POST , instance = need)
        if req.is_valid():
            req.save()
            return HttpResponseRedirect('/') 
    else:
        need = StudentModel.objects.get(pk= id)
        req = StudentModelForm(instance = need)
        return render(request,'update.html',{'form':req})

