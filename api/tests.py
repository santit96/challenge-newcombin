import json
from django.test import TestCase
from rest_framework.test import APIClient

from .models.payable import Payable
from .models.transaction import Transaction


class ApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.barcode = 123456789
        self.payable = Payable.objects.create(
            barcode=self.barcode,
            service_type="water",
            service_description="a service",
            expiration="2022-12-12",
            amount=100,
            status="pending"
        )
        self.transaction = Transaction.objects.create(
            payment_method="credit_card",
            card_number=1234556789,
            amount=100,
            payment_date="2022-11-12",
            barcode=self.payable
        )
        self.num_payables = Payable.objects.filter(status="pending").count()
        self.num_transactions = Transaction.objects.group_by_day().count()

    def test_list_payable(self):
        response = self.client.get(
            '/api/payables',
            format='json',
        )
        content = json.loads(response.content)
        self.assertEqual(len(content), self.num_payables)
        self.assertEqual(response.status_code, 200)

    def test_list_transaction(self):
        response = self.client.get(
            '/api/transactions',
            format='json',
        )
        content = json.loads(response.content)
        self.assertEqual(len(content), self.num_transactions)
        self.assertEqual(response.status_code, 200)
