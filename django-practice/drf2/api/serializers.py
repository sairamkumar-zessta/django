from rest_framework import serializers
from .models import Student

class StudentSerilizer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    father_name = serializers.CharField(max_length = 100)
    class_name = serializers.IntegerField()
    date_of_birth = serializers.DateField(null = True) 


def create(self,validate_data):
    return Student.objects.create(**validate_data) 
    