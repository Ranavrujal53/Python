from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def blog_grid(request):
    return render(request,"blog-grid.html")

def blog_single(request):
    return render(request,"blog-single.html")

def error(request):
    return render(request,"error.html")

def signin(request):
    return render(request,"signin.html")

def signup(request):
    return render(request,"signup.html")