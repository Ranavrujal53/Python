from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_page(request):
    if request.method == "POST":
        data = request.POST
        uname = data.get('uname')
        password = data.get('password')

        u = authenticate(username=uname,password=password)
        if u is None:
            return render(request,"login.html",{"err":"invalid data"})
        else:
            login(request,u)
            return redirect("home")
        
    if request.user.is_authenticated:
        return render(request,"home.html")
    return render(request,"login.html")

def reg_page(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        uname = data.get('uname')
        email = data.get("email")
        password = data.get("password")

        if  User.objects.filter(username=uname).exists():
            return render(request,"reg.html",{"err":"Username exist !!!"})
        
        u = User(first_name=name,username=uname,email=email)
        u.set_password(password)
        u.save()

        return render(request,"reg.html",{"msg":"Registration successful"})
    
    return render(request,"reg.html")
    

@login_required(login_url="loginpage")
def home(request):
    return render(request,"home.html")

def user_logout(request):
    
    logout(request)
    return redirect("loginpage")