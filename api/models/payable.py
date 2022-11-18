from django.db import models

class Payable(models.Model):
    barcode = models.BigIntegerField(primary_key=True)
    service_type = models.CharField(max_length=50)
    service_description = models.CharField(max_length=150)
    expiration = models.DateField()
    amount = models.IntegerField()
    status = models.CharField(max_length=20)
