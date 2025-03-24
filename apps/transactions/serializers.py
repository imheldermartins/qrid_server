from rest_framework import serializers

from .models import Transaction

from apps.categories.serializers import CategorySerializer


class TransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ("owner", "wallet_monthly", "category")
