from django.db import models
from django.contrib.auth.models import AbstractUser
from myapp.manager import *
# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=20)

class CustomeUser(AbstractUser):
    username = None
    phone = models.CharField(max_length=20,unique=True)