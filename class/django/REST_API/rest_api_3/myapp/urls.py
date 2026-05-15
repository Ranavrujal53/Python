from django.urls import path
from myapp.views import *

urlpatterns = [
    path("get",get_data,name="get")
]
