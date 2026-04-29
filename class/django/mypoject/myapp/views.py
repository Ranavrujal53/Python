from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib import messages 
# Create your views here.
def index(request):
    s = Stud.objects.all()
    if request.method =="POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")

        Stud.objects.create(name=name,email=email,age=age)
        # return render(request, "index.html", {'msg': 'data inserted','std':s})
        messages.success(request,"data inserted")
        return redirect("index")

    return render(request,"index.html",{'std':s})

def delete(request):
    dele = request.GET['dele']
    st=Stud.objects.get(id=dele)
    st.delete()
    return redirect("index")


def update(request):
    s = Stud.objects.all()
    if request.method =="POST":
        data = request.POST
        id = data.get("id")
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")

        st = Stud.objects.get(id=id)
        st.name = name
        st.email = email
        st.age = age
        st.save()

        return redirect("index")
    uid = request.GET['uid']
    st = Stud.objects.get(id = uid)
    return render(request,"index.html",{'stud':st,'std':s,'msg':'data update'})
