from api.models.transaction import Transaction
from api.serializers.transaction_serializer import TransactionSerializer
from api.serializers.transaction_list_serializer import TransactionListSerializer
from rest_framework import generics
from django.db.models import Count, Sum
from django.db.models.functions import TruncDay
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django.core.exceptions import ValidationError


class TransactionsFilter(SearchFilter):

    def filter_queryset(self, request, queryset, view):
        queryset = super().filter_queryset(request, queryset, view)
        return queryset.annotate(
            day=TruncDay('payment_date')
        ).values('day').annotate(count=Count('id'), total_amount=Sum('amount')).values('day', 'count', 'total_amount')


class TransactionsView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    list_serializer_class = TransactionListSerializer
    filter_backends = TransactionsFilter

    def list(self, request):
        queryset = self.filter_backends().filter_queryset(request, self.queryset, self)
        #data = self.list_serializer_class(queryset, many=True).data
        return Response(queryset)
