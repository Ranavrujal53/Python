from django.shortcuts import render,redirect
from myapp.models import *
import os
# Create your views here.
def index(request):
    emp = Emp.objects.all() 
    if request.method =="POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        dept = data.get("dept")
        image = request.FILES.get("file")

        Emp.objects.create(name=name,email=email,phone=phone,dept=dept,image=image)

        # return render(request,"index.html",{'msg':'data successuly inserted'})
        return redirect("index")
    return render(request,"index.html",{'emp':emp})

def delete(request):
    did = request.GET['did']
    em = Emp.objects.get(id=did)
    os.remove(em.image.path)
    em.delete()
    return redirect(index)

def update(request):
    emp = Emp.objects.all() 
    if request.method =="POST":
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        dept = data.get("dept")

        em = Emp.objects.get(id=id)
        em.name = name
        em.email = email
        em.phone = phone
        em.dept = dept
        if request.FILES:
            image = request.FILES.get("file")
            os.remove(em.image.path)
            em.image = image
        em.save()

        return redirect('index')
    
    uid = request.GET['uid']
    em=Emp.objects.get(id=uid)
    return render(request,"index.html",{'emps':em,'emp':emp})