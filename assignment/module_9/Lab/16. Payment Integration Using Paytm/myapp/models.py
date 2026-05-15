from django.db import models

class Doctor(models.Model):

    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    fees = models.IntegerField()

    def __str__(self):
        return self.name


class Payment(models.Model):

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    customer_name = models.CharField(max_length=100)

    amount = models.IntegerField()

    payment_status = models.CharField(max_length=50)

    transaction_id = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name