from django.db import models


class Transaction(models.Model):
    PAYMENT_METHODS = (
        ("CASH", "Cash"),
        ("CREDIT-CARD", "CC"),
        ("DEBIT-CARD", "DC"),
        ("BANK-TRANSFER", "BT"),
        ("PAYPAL", "Paypal"),
        ("PIX", "Pix"),
        ("OTHER", "Other"),
    )

    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    tags = models.JSONField(default=list, blank=True)
    payment_method = models.CharField(
        blank=False, choices=PAYMENT_METHODS, default="CASH", max_length=20
    )
    amount = models.FloatField(default=0, null=False, blank=False)
    scheduled_date = models.DateField(null=False, blank=False, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    category_id = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, null=False
    )
    wallet_monthly_id = models.ForeignKey(
        "wallet_monthly_summary.WalletMonthlySummary",
        on_delete=models.CASCADE,
        null=False,
    )

    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = "transactions"
