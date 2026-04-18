from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",product,name="product"),
    path("stud",student,name="student"),
    path("emp",emp,name="emp")
]
