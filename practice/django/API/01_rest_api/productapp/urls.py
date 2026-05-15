from django.urls import path
from productapp.views import *

urlpatterns = [
    path("product",productview.as_view()),
    path("product/<id>",productviewRetrive.as_view()),


    path("category",categoryview.as_view()),
    path("category/<id>",categoryviewRetrive.as_view()),

    path("product/category/<id>",product_by_category)
]

