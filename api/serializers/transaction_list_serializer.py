from api.models.transaction import Transaction
from rest_framework import serializers

class TransactionListSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    total_amount = serializers.IntegerField()
    day = serializers.DateField()
