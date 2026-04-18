from django.urls import path
from solar_app.views import *

urlpatterns = [
    path("",index,name="index"),
    path("error_data",error,name="error_data"),
    path("about",about,name="about"),
    path("contact",contact,name="contact"),
    path("feature",feature,name="feature"),
    path("project",project,name="project"),
    path("quote",quote,name="quote"),
    path("services",services,name="services"),
    path("team",team,name="team"),
    path("testimonial",testimonial,name="testimonial")
]
