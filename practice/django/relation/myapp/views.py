from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def index(request):
    categories = Category.objects.all()
    product = Product.objects.all()
    return render(request,"index.html",{'categories':categories,"product":product})

def add_product(request):
    if request.method == "POST":
        data = request.POST
        category = data.get("category")
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")

        catobj = Category.objects.get(id=category)
        Product.objects.create(category=catobj,name=name,price=price,qty=qty)

        return redirect("index")


def update(request):
    
