from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib import messages   
# Create your views here.
def student(request):
    stud = Stud.objects.all()
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")

        Stud.objects.create(name=name,email=email,age=age)
        # return render(request,"student.html",{'msg':'data successfully inserted','stud':stud})
        messages.success(request, "Data Successfully Inserted")
        return redirect("student")
    return render(request,"student.html",{'stud':stud})

def delete(request):
    dell = request.GET['dell']
    st =Stud.objects.get(id=dell)
    st.delete()
    return redirect("student")

def update(request):
    stud = Stud.objects.all()   
    if request.method == "POST":
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
        
        return render(request, "student.html",{'msg': 'Data successfully updated','stud': stud })

    uid = request.GET['uid']
    st = Stud.objects.get(id=uid)
    return render(request,"student.html",{"stu":st,"stud":stud})
    




def emp(request):
    em = Emp.objects.all()
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        dept = data.get("dept")
        salary = data.get("salary")

        Emp.objects.create(name=name,email=email,dept=dept,salary=salary)
        # return render(request,"student.html",{'msg':'data successfully inserted'},{'stud':stud})
        return redirect("emp")
    return render(request,"emp.html",{'em':em,'msg':'Employee data successfuly inserted'})


def pro(request):
    pr = Product.objects.all()
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        price = data.get("price")
        stock = data.get("stock")

        Product.objects.create(name=name,price=price,stock=stock)
        # return render(request,"student.html",{'msg':'data successfully inserted'},{'stud':stud})
        return redirect("product")
    return render(request,"product.html",{'pr':pr,'msg':'Product data successfuly inserted'})


