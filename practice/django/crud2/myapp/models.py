from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

