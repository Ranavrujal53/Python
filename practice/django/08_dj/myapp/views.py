from django.shortcuts import render
from .models import Register, Order

def home(request):
    msg = ""

    # REGISTER
    if request.method == "POST" and "register" in request.POST:
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if name and email and password:
            Register.objects.create(name=name, email=email, password=password)
            msg = "Registration Successful"

    # LOGIN
    if request.method == "POST" and "login" in request.POST:
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = Register.objects.filter(email=email, password=password).first()

        if user:
            msg = f"Welcome {user.name}"
        else:
            msg = "Invalid Login"

    # ORDER
    if request.method == "POST" and "order" in request.POST:
        product = request.POST.get("product")
        quantity = request.POST.get("quantity")

        if product and quantity:
            Order.objects.create(product=product, quantity=quantity)
            msg = "Order Placed"

    users = Register.objects.all()
    orders = Order.objects.all()

    return render(request, "view.html", {
        "msg": msg,
        "users": users,
        "orders": orders
    })