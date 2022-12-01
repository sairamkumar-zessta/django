from django import forms
from .models import Student
class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Student 
        fields='__all__'
class VendorForm(forms.Form):
    name=forms.CharField()
    address=forms.CharField()
    contactdetails=forms.CharField()
    item=forms.CharField()