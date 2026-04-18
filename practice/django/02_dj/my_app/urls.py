from django.urls import path
from my_app.views import *

urlpatterns = [
    path("",index,name="index"),
    path("about",about,name="about"),
    path("blog_list",blog_list,name="blog_list"),
    path("contact",contact,name="contact"),
    path("product",product,name="product"),
    path("testimonial",testimonial,name="testimonial"),
]
