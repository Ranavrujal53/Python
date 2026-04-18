from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price= models.IntegerField()
    stock = models.IntegerField()
    dec = models.CharField(max_length=20)

class Stud(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    age = models.FloatField()
    std = models.CharField(max_length=20)

class Emp(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    salary = models.FloatField()
    dept = models.CharField(max_length=20)