from django.db import models

class PaymentMethodEnum(models.TextChoices):

    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    CASH = "cash"
