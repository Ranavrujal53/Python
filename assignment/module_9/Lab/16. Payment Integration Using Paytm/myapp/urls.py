from django.urls import path
from myapp.views import *

urlpatterns = [

    path('', home),

    path('payment/<int:id>/', payment_page),

    path('success/', success),

    path('failed/', failed),
]