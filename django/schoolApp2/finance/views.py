from django.shortcuts import render

# Create your views here.
def feePay(request):
    return render(request,'finance/fee_pay.html')
def feePaidRep(request):
    return render(request,'finance/fee_paid_rep.html')
def feeDue(request):
    return render(request,'finance/feee_due.html')