from django.urls import path
from myapp.views import *
urlpatterns = [
    path('', index, name="index"),
    path('show/', show, name="show"),
    path('delete/<int:id>/', delete, name="delete"),
    path('edit/<int:id>/', edit, name="edit"),
    path('update/<int:id>/', update, name="update"),
]