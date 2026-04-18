from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('addproduct/', views.add_product, name="addproduct"),
    path('addcategory/', views.add_category, name="addcategory"),
]