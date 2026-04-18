from django.urls import path
from my_app.views import *
urlpatterns = [
    path("",index,name="index"),
    path("blog-grid",blog_grid,name="blog-grid"),
    path("blog-single",blog_single,name="blog-single"),
    path("error",error,name="error"),
    path("signin",signin,name="signin"),
    path("signup",signup,name="signup")
]
