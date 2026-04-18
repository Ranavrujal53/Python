from django.shortcuts import render
from website.models import *

# Create your views here.
def index(request):
    if request.method=="POST":
        data=request.POST
        name=data.get("name")
        email=data.get("email")
        age=data.get("age")
        dob=data.get("dob")
        Student.objects.create(name=name,email=email,age=age,dob=dob) 

        return render(request,"index.html",{"meg":"Registration is success"}) 
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"service.html")