from django.db import models


class WalletMonthlySummary(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()
    total_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_incomes = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    wallet = models.ForeignKey("wallets.Wallet", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("month", "year", "wallet_id")
        db_table = "wallet_monthly_summary"

    def __str__(self):
        return f"{self.wallet_id} - {self.month}/{self.year}"
