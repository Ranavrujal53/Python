from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        u = authenticate(username=username,password=password)
        if u is None:
            return render(request,"login.html",{'err':"invalid"})
        else:
            login(request,u)

        return redirect("home")
    return render(request,"login.html")
    
def reg_page(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            return render(request, "reg.html", {'err': "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request,"reg.html",{'err':"username exits"})
        
        u = User(first_name=name,email=email,password=password,username=username)

        u.set_password(password)
        u.save()

        return render(request,"reg.html",{"msg":"Registartion successfullt"})
    return render(request,"reg.html")

@login_required(login_url="loginpage")
def home(request):
    return render(request,"home.html")

def user_logout(request):
    logout(request)
    return redirect("loginpage")

