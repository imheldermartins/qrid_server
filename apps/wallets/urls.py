from django.urls import path
from .views import WalletCreateView

urlpatterns = [
    # path(
    #     "", TransactionListView.as_view(), name="transactions-list"
    # ),  # /api/transactions/
    # path(
    #     "<int:id>/", TransactionDetailView.as_view(), name="transaction-detail"
    # ),  # /api/transactions/:id/
    path(
        "create/", WalletCreateView.as_view(), name="wallet-create"
    ),  # /api/transactions/create/
]
