from django.shortcuts import render
from studentapp.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from studentapp.serializer import *
# Create your views here.

@api_view(['GET'])
def get_student(request):
    students = Student.objects.all()
    ser = Studentserilizer(students,many=True)
    return Response({"data":ser.data})

@api_view(['POST'])
def post_student(request):
    ser = Studentserilizer(data = request.data)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"sommthing went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"data inserted successfully"})
    
@api_view(["PUT"])
def put_student(request,id):
    student = Student.objects.get(id=id)
    ser = Studentserilizer(student,request.data,partial=True)
    if not ser.is_valid():
        return Response({"errors":ser.errors,"message":"sommthing went wrong"})
    else:
        ser.save()
        return Response({"data":ser.data,"message":"data update successfully"})

@api_view(["DELETE"])
def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response({"message":"Student Delete"})