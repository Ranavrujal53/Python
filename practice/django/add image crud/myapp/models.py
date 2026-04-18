from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images",null=True)
    