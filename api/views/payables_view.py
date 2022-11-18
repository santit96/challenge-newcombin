from api.models.payable import Payable
from api.serializers.payable_serializer import PayableSerializer
from rest_framework import generics

class PayablesView(generics.ListCreateAPIView):
    queryset = Payable.objects.filter(status="pending")
    serializer_class = PayableSerializer
    filterset_fields = ['service_type']
