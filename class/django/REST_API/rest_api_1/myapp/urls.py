from django.urls import path
from rest_api_1.myapp.views import example_view

urlpatterns = [
    path('', example_view, name='example'),
]