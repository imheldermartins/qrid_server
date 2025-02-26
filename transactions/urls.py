from django.urls import path
from .views import TransactionListView, TransactionDetailView

urlpatterns = [
    path(
        "", TransactionListView.as_view(), name="transactions-list"
    ),  # /api/transactions/
    path(
        "<int:id>/", TransactionDetailView.as_view(), name="transaction-detail"
    ),  # /api/transactions/:id
]
