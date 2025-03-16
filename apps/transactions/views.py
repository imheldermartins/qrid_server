from decimal import Decimal

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from apps.wallet_monthly_summary.utils import get_previous_wallet_summary

from .models import Transaction
from .serializers import TransactionSerializer
from apps.wallet_monthly_summary.models import WalletMonthlySummary
from apps.wallets.models import Wallet

from apps.categories.models import Category
from apps.categories.utils import is_credit, is_debit


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
        # Obtendo os dados do request
        wallet_id = self.request.data.get("wallet_id")
        category_id = self.request.data.get("category_id")
        scheduled_date = self.request.data.get("scheduled_date")
        amount = self.request.data.get("amount")

        # Converte o valor de `amount` para evitar erro de tipagem e flutuação
        amount = Decimal(str(amount))

        if not wallet_id or not scheduled_date:
            raise serializers.ValidationError(
                "wallet_id and scheduled_date são campos obrigatórios"
            )

        year, month, _ = map(int, scheduled_date.split("-"))

        # Obtendo a Wallet
        wallet = get_object_or_404(Wallet, id=wallet_id)
        category = get_object_or_404(Category, id=category_id)

        owner = self.request.user

        previous_summary = get_previous_wallet_summary(wallet, year, month)

        # Criando ou obtendo a WalletMonthlySummary
        wms, created = WalletMonthlySummary.objects.get_or_create(
            wallet=wallet,
            month=month,
            year=year,
            defaults={
                "total_balance": (
                    previous_summary.total_balance + amount
                    if previous_summary
                    else amount if is_credit(category.type) else -amount
                ),
                "total_incomes": amount if is_credit(category.type) else 0.0,
                "total_expenses": amount if is_debit(category.type) else 0.0,
            },
        )

        # Se for débito, validamos o saldo corretamente ANTES de permitir a transação
        if is_debit(category.type):
            if created:
                # Se a carteira atual foi criada agora, validamos com o saldo do mês anterior
                previous_balance = (
                    previous_summary.total_balance if previous_summary else 0.0
                )
                new_balance = previous_balance - amount
            else:
                # Se a carteira já existia, usamos o saldo dela
                new_balance = wms.total_balance - amount

            # Se o saldo for insuficiente, BLOQUEAMOS a transação
            if new_balance < 0:
                raise serializers.ValidationError(
                    'Você não possui saldo suficiente nesta carteira. (Se desejar habilitar transações sem restrições, acesse o menu "Limites")'
                )

        if not created:
            if is_credit(category.type):
                wms.total_balance += amount
                wms.total_incomes += amount
            elif is_debit(category.type):
                wms.total_balance -= amount
                wms.total_expenses += amount
            wms.save()

        # Criando a transação com a WalletMonthlySummary correta
        serializer.save(
            wallet_monthly=wms,
            owner=owner,
            scheduled_date=scheduled_date,
            category=category,  # 🔥 Corrigindo a ausência da categoria
        )
