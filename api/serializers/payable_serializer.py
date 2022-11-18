from api.models.payable import Payable
from rest_framework import serializers

class PayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payable
