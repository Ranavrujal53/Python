from django.urls import path
from productapp.views import *

urlpatterns = [
    path("all/", ProductView.as_view()),
    path("all<id>", ProductDetailView.as_view()),
]
