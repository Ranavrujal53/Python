from django.urls import path
from clothe_app.views import *
urlpatterns = [
    path("",index,name="index"),
    path("about",about,name="about"),
    path("blog-detail",blog_detail,name="blog-detail"),
    path("blog",blog,name="blog"),
    path("contact",contact,name="contact"),
    path("home-02",home_02,name="home-02"),
    path("home-03",home_03,name="home-03"),
    path("product-detail",product_detail,name="product-detail"),
    path("product",product,name="product"),
    path("product-detail",product_detail,name="shoping-cart"),
]
