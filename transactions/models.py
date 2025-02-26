from django.db import models


class Transaction(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=500, blank=True)
    amount = models.FloatField(default=0, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
