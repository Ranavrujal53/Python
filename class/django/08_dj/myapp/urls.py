from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("emp",emp,name="emp"),
    path("product",product,name="product"),
]
