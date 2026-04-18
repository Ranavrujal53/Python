from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
def index(request):
    emp = Emp.objects.all()
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        dept = data.get("dept")

        Emp.objects.create(name=name,email=email,dept=dept)

        # return render(request,"index.html")
        return redirect("index")
    return render(request,"index.html",{'emp':emp,'msg':'data successfull store'})

def delete(request):
    dele = request.GET['dele']
    em = Emp.objects.get(id = dele)
    em.delete()
    return redirect("index")


def update(request,id):
    emp =Emp.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        emp.name = data.get("name")
        emp.email = data.get("email")
        emp.dept = data.get("dept")
        emp.save()

        return redirect("index")
    
    return render(request,"update.html",{"emp":emp})

