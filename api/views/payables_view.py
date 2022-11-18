from api.models.payable import Payable
from api.serializers.payable_serializer import PayableSerializer
from rest_framework import generics

class PayablesView(generics.ListAPIView):
    queryset = Payable.objects.all()
    serializer_class = PayableSerializer
