from django.db import models

from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100)
    price = models.FloatField(default=0, null=False)
    rated = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
