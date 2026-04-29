from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse,HttpResponse
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,"index.html")

def display(request):
    student = Student.objects.all()
    return JsonResponse({"student":list(student.values())})

def add_user(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")

        Student.objects.create(name=name,email=email,age=age)

        return HttpResponse("Registration Successfully !!")