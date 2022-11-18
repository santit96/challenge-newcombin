from django.urls import path

from .views import payables_view

urlpatterns = [
    path('', payables_view.PayablesView.as_view(), name='api'),
]
