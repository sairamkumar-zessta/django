from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerilizer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        serializer = StudentSerilizer(pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Created' }
            json_data = JSONRenderer().render(serializer) 
            return HttpResponse(json_data, content_type = 'application/json')