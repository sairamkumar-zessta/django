from functools import partial
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from home.serializers import peopleSerializer
from home.models import Person
from rest_framework.views import APIView
# Create your views here.

@api_view(['GET','POST','PUT','PATCH'])
def person(request):
    if request.method=='GET':
        objs= Person.objects.all() 
        serializer= peopleSerializer(objs, many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data=request.data 
        serializer = peopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors) 
    elif request.method == "PUT":
        data=request.data
        serializer = peopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors) 
    elif request.method == "PATCH":
        data=request.data
        obj=Person.objects.get(id=data['id'])
        serializer = peopleSerializer(obj, data = data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors) 
