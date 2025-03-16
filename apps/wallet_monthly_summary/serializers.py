from rest_framework import serializers

from .models import WalletMonthlySummary


class WalletMonthlySummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = WalletMonthlySummary
        fields = "__all__"

    def create(self, validated_data):
        return WalletMonthlySummary.objects.create(**validated_data)
