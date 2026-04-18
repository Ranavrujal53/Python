from django.shortcuts import render
from myapp.models import *
# Create your views here.

def index(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")

        Stud.objects.create(name=name,email=email,age=age)
        return render(request,"index.html",{"msg":"data successfult add"})
    data = Stud.objects.all()
    return render(request,"index.html",{"data":data})

    return render(request,"index.html")

    

def emp(request):
    if request.method =="POST":
        data = request.POST
        name = data.get("name")
        salary = data.get("salary")
        dept = data.get("dept")

        Emp.objects.create(name=name,salary=salary,dept=dept)
        return render(request,"emp.html",{"msg":"emp data successfully add"})
    
    data = Emp.objects.all()
    return render(request,"emp.html",{"data":data})
    return render(request,"emp.html")
