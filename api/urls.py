from django.urls import path

from .views import payables_view, transactions_view

urlpatterns = [
    path('payables', payables_view.PayablesView.as_view(), name='payables'),
    path('transactions', transactions_view.TransactionsView.as_view(), name='transactions'),
]
