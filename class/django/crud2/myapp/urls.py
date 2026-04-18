from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",student,name="student"),
    path("delete",delete,name="delete"),
    path("update",update,name="update"),
    path("emp",emp,name="emp"),
    path("product",pro,name="product")
]
