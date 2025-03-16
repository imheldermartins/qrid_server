from django.urls import path
from .views import TransactionCreateView, TransactionListView, TransactionDetailView

urlpatterns = [
    path(
        "", TransactionListView.as_view(), name="transactions-list"
    ),  # /api/transactions/
    path(
        "<int:id>/", TransactionDetailView.as_view(), name="transaction-detail"
    ),  # /api/transactions/:id/
    path(
        "create/", TransactionCreateView.as_view(), name="transaction-create"
    ),  # /api/transactions/create/
]
