from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("addproduct",add_product,name="addproduct"),
    path("update",update,name="update"),
]
