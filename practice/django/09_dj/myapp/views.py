from django.shortcuts import render, redirect
from myapp.models import *

# HOME PAGE
def home(request):
    return render(request, "home.html")


# REGISTRATION
def regs(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        email = data.get("email")
        mobilenumber = data.get("mobilenumber")
        password = data.get("password")
        address = data.get("address")
        dob = data.get("dob")

        if Reg.objects.filter(username=username).exists():
            return render(request, "registration.html", {"msg": "Username already exists"})

        Reg.objects.create(
            username=username,
            email=email,
            mobilenumber=mobilenumber,
            password=password,
            address=address,
            dob=dob
        )

        return redirect('login')   # ✅ after register → login

    return render(request, "registration.html")


# LOGIN
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = Reg.objects.get(username=username, password=password)

            request.session['username'] = user.username

            return redirect('home')   # ✅ back to home

        except Reg.DoesNotExist:
            return render(request, "login.html", {"msg": "Invalid Username or Password"})

    return render(request, "login.html")


# LOGOUT
def logout(request):
    request.session.flush()
    return redirect('home')