from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def error(request):
    return render(request, "error_data.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def feature(request):
    return render(request,"feature.html")

def project(request):
    return render(request,"project.html")

def quote(request):
    return render(request,"quote.html")

def services(request):
    return render(request,"services.html")

def team(request):
    return render(request,"team.html")

def testimonial(request):
    return render(request,"testimonial.html")