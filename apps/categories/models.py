from django.db import models


class Category(models.Model):
    INCOME = "income"
    EXPENSE = "expense"
    TYPE = ((INCOME, "INCOME"), (EXPENSE, "EXPENSE"))

    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, default="grey")
    icon = models.CharField(max_length=255, default="tag")
    type = models.CharField(max_length=255, choices=TYPE, default="income")
    owner = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"
