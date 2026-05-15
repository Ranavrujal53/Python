from django.shortcuts import render
from myapp.models import *
# Create your views here.

def home(request):
    return render(request,"index.html")
