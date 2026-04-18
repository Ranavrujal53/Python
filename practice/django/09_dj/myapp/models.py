from django.db import models

# Create your models here.
class Reg(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    mobilenumber = models.IntegerField()
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    dob = models.DateField()