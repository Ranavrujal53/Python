from django.urls import path
from food_app.views import *
urlpatterns = [
    path("",index,name="index"),
    path("about",about,name="about"),
    path("book",book,name="book"),
    path("menu",menu,name="menu"),
]
