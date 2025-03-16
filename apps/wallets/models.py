from django.db import models


class Wallet(models.Model):
    name = models.CharField(max_length=100)

    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} (ID={self.id})"

    class Meta:
        verbose_name_plural = "Wallets"
        db_table = "wallets"
