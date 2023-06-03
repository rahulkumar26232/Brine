from django.contrib.auth.models import User
from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PriceAlert(models.Model):
    class TextChoices(models.TextChoices):
        created = 'created', 'Created'
        deleted = 'deleted', 'Deleted'
        triggered = 'triggered', 'Triggered'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_price = models.IntegerField()
    status = models.CharField(max_length=20, choices=TextChoices.choices, default=TextChoices.created)
    created_at = models.DateTimeField(auto_now_add=True)
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE)

