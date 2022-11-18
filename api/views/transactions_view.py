from api.models.transaction import Transaction
from api.serializers.transaction_serializer import TransactionSerializer
from api.serializers.transaction_list_serializer import TransactionListSerializer
from rest_framework import generics 

class TransactionsView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    list_serializer_class = TransactionListSerializer
    filterset_fields = {
        'payment_date':['gte', 'lte', 'exact', 'gt', 'lt'],
    }

    def get_queryset(self):
        return Transaction.objects.group_by_day()

    def list(self, request):
        self.serializer_class = TransactionListSerializer
        return super().list(request)
