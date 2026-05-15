from django.urls import path
from myapp.views import *

urlpatterns = [
    path("doctors/",DoctorView.as_view()),
    path("doctors/<int:id>/",DoctorViewRetrive.as_view())
]
