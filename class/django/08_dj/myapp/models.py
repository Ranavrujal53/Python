from django.db import models

# Create your models here.
class Stud(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    age = models.IntegerField()

class Emp(models.Model):
    name = models.CharField(max_length=20)
    salary = models.FloatField()
    dept = models.CharField(max_length=20)
    addess = models.CharField(max_length=20)

class Pro(models.Model):
    pr_name = models.CharField(max_length=20)
    quntity = models.IntegerField()
    price = models.FloatField()
    stock = models.IntegerField()