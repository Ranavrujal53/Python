from django.shortcuts import render
from myapp.models import *

# Create your views here.
def product(request):
    if request.method =="POST":
        data = request.POST

        name = data.get("name")
        price = data.get("price")
        stock = data.get("stock")
        dec = data.get("dec")

        Product.objects.create(name=name,price=price,stock=stock,dec=dec)

        return render(request,"product.html",{'meg':'Product data successfully inserted'})

    return render(request,"product.html")

def student(request):

    if request.method =="POST":
        data = request.POST

        name = data.get("name")
        email = data.get("email")
        age = data.get("age")
        std = data.get("std")

        Stud.objects.create(name=name,email=email,age=age,std=std)

        return render(request,"student.html",{'meg':'Student data successfully inserted'})
    return render(request,"student.html")

def emp(request):

    if request.method =="POST":
        data = request.POST

        name = data.get("name")
        email = data.get("email")
        salary = data.get("salary")
        dept = data.get("dept")

        Emp.objects.create(name=name,email=email,salary=salary,dept=dept)

        return render(request,"emp.html",{'meg':'Employee data successfully inserted'})
    return render(request,"emp.html")