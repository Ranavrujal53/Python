from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    age = models.IntegerField()
    dob = models.DateField()

class emp(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=50)
    emp_age = models.IntegerField()
    emp_dept = models.CharField(max_length=20)

class product(models.Model):
    pr_name = models.CharField(max_length=20)
    pr_items = models.IntegerField()
    pr_sepecification = models.CharField(max_length=30)
    

    