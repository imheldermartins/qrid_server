from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Transaction
from .serializers import TransactionSerializer
from apps.wallet_monthly_summary.models import WalletMonthlySummary
from apps.wallets.models import Wallet


class TransactionListView(generics.ListAPIView):
    """(GET)
    Get all objects on transactions schema
    """

    permission_classes = (IsAuthenticated,)

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailView(generics.RetrieveAPIView):
    """(GET)
    Get a only transaction based on <int:id> param
    """

    permission_classes = (IsAuthenticated,)

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "id"


class TransactionCreateView(generics.CreateAPIView):
    """(POST)
    Create a new transaction
    """

    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        # Get wallet_id, month and year from request data
        wallet_id = self.request.data.get("wallet_id")
        scheduled_date = self.request.data.get("scheduled_date")

        if not wallet_id or not scheduled_date:
            raise serializers.ValidationError(
                "wallet_id and scheduled_date are required fields"
            )

        year, month, _ = map(int, scheduled_date.split("-"))

        # Get wallet object
        wallet = get_object_or_404(Wallet, id=wallet_id)

        print(wallet)

        wms, created = WalletMonthlySummary.objects.get_or_create(
            wallet=wallet,
            month=month,
            year=year,
        )

        serializer.save(
            wallet=wms,
            account=self.request.user,
            scheduled_date=scheduled_date,
            owner=self.request.user,
        )
        return super().perform_create(serializer)
