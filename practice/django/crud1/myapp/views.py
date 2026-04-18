from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib import messages
# Create your views here.

def index(request):
    s=Student.objects.all()
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")

        Student.objects.create(name=name,email=email,age=age)
        messages.success(request,"data inserted")
        return redirect("index")
    return render(request,"index.html",{'std':s})


#Delete

def delete(request):
    dele = request.GET['dele']
    st=Student.objects.get(id=dele)
    st.delete()
    return redirect("index")


#Update

def update(request):
    s= Student.objects.all()
    if request.method == "POST":
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")


        st = Student.objects.get(id=id)
        st.name=name
        st.email = email
        st.age = age
        st.save()

        return redirect('index')
    
    uid = request.GET['uid']
    st=Student.objects.get(id = uid)
    return render(request,"index.html",{'stud':st,'std':s,'message':'data update'})