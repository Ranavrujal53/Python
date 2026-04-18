from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', home, name='home'),
    path('registration/', regs, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/',logout, name='logout'),
]