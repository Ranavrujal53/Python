from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import *
# Create your views here.

def index(request):
    return render(request,"index.html")

def test(request):
    uname = request.GET['uname']
    return HttpResponse(f"Hello {uname}")

def search(request):
    q = request.GET['q']
    pro = "<ul>"

    products = Product.objects.filter(name__startswith=q)

    for i in products:
        pro += f"<li>{i.name}</li>"
        
    pro += "</ul>"

    return HttpResponse(pro)
    
def countries(request):
    all_countries = Country.objects.all()
    return JsonResponse({"data":list (all_countries.values())})

def states(request):
    cid = request.GET['cid']
    country = Country.objects.get(pk=cid)
    all_states = State.objects.filter(country=country)
    return JsonResponse({"data":list(all_states.values())})


def cities(request):
    sid = request.GET['sid']
    state = State.objects.get(pk=sid)
    all_cities = City.objects.filter(state=state)
    return JsonResponse({"data": list(all_cities.values())})