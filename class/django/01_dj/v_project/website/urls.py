from django.urls import path
from website.views import *

urlpatterns = [
    path("",index,name='index'),
    # path("index/",index,name='index'),
    path("about/",about,name='about'),
    path("service/",service,name='service'),
]
