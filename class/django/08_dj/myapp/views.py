from django.shortcuts import render
from myapp.models import *
# Create your views here.
def index(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")

        
        Stud.objects.create(name=name,email=email,age=int(age))
        if name and email and age:
            return render(request,"emp.html",{"msg":"Data successfuly insrted"})
        else:
            return render(request, "index.html", {"msg": "All fields are required!"})
    return render(request,"index.html")



def emp(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        salary = data.get("salary")
        dept = data.get("dept")
        addess = data.get("addess")

        Emp.objects.create(name=name,salary=salary,dept=dept,addess=addess)
        if name and salary and dept and addess:
            return render(request,"product.html",{"msg":"Emp Data successfuly insrted"})
        else:
            return render(request,"emp.html",{"msg":"Employee all data required"})
    return render(request,"emp.html")


def product(request):
    if request.method == "POST":
        data = request.POST
        pr_name = data.get("pr_name")
        quntity = data.get("quntity")
        price = data.get("price")
        stock = data.get("stock")

        Pro.objects.create(pr_name=pr_name,quntity=quntity,price=price,stock=stock)
        if pr_name and quntity and price and stock:
            return render(request,"index.html",{"msg":"Product Data successfuly insrted"})
        else:
            return render(request,"product.html",{"msg":"product all data are required"})
    return render(request,"product.html")