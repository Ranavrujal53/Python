from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)
    specialty = models.CharField(max_length=20)
    experience = models.IntegerField()
    available = models.CharField(max_length=20)

    def __str__(self):
        return self.name