from api.models.transaction import Transaction
from api.serializers.transaction_serializer import TransactionSerializer
from rest_framework import generics

class TransactionsView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
