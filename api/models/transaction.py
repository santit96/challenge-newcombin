from django.db import models
from api.models.payable import Payable
from api.models.payment_method_enum import PaymentMethodEnum

class Transaction(models.Model):
    payment_method = models.CharField(max_length=25, choices=PaymentMethodEnum.choices)
    card_number = models.IntegerField()
    amount = models.IntegerField()
    barcode = models.ForeignKey(Payable, on_delete=models.PROTECT, related_name='payments')
    payment_date = models.DateField()
