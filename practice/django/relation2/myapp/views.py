from django.shortcuts import render, redirect
from myapp.models import Category, Product


# INDEX PAGE (Product + Category dropdown)
def index(request):
    categories = Category.objects.all()
    product = Product.objects.all()

    return render(request, "index.html", {
        'categories': categories,
        'product': product
    })


# ADD PRODUCT
def add_product(request):
    if request.method == "POST":
        category_id = request.POST.get("category")
        name = request.POST.get("name")
        price = request.POST.get("price")
        qty = request.POST.get("qty")

        if category_id == "0":
            return redirect("index")

        catobj = Category.objects.get(id=category_id)

        Product.objects.create(
            category=catobj,
            name=name,
            price=price,
            qty=qty
        )

    return redirect("index")


# ADD CATEGORY (Separate Form)
def add_category(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Category.objects.create(name=name)
        return redirect("addcategory")

    categories = Category.objects.all()
    return render(request, "category.html", {"categories": categories})