from django.shortcuts import render, redirect
from myapp.models import *
from django.contrib import messages
import os

# Create your views here.

def index(request):
    c = Coffee.objects.all()

    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        price = data.get("price")
        category = data.get("category")
        image = request.FILES.get("file")

        Coffee.objects.create(
            name=name,
            price=price,
            category=category,
            image=image
        )

        messages.success(request, "data inserted ")
        return redirect("index")

    return render(request, "index.html", {'coffee': c})


def delete(request):
    did = request.GET['did']
    co = Coffee.objects.get(id=did)

    if co.image and os.path.exists(co.image.path):
        os.remove(co.image.path)

    co.delete()
    return redirect("index")


def update(requset):
    c = Coffee.objects.all()

    if requset.method == "POST":
        data = requset.POST
        id = data.get("id")
        name = data.get("name")
        price = data.get("price")
        category = data.get("category")

        co = Coffee.objects.get(id=id)
        co.name = name
        co.price = price
        co.category = category

        if requset.FILES:
            image = requset.FILES.get("file")

            if co.image and os.path.exists(co.image.path):
                os.remove(co.image.path)

            co.image = image

        co.save()
        return redirect("index")

    uid = requset.GET['uid']
    co = Coffee.objects.get(id=uid)

    return render(requset, "index.html", {'coff': co, "coffee": c})