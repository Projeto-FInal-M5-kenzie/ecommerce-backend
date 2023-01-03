from django.db import models

# Create your models here.


class PaymentsOptions(models.TextChoices):
    PIX = "Pix"
    CARD = "Card"
    DEFAULT = "Not informed"


class Payment(models.Model):
    method_payment = models.CharField(
        max_length=30,
        choices=PaymentsOptions.choices,
        default=PaymentsOptions.DEFAULT,
    )
    total_price = models.FloatField()
    done = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    client = models.ForeignKey(
        "clients.Client",
        on_delete=models.CASCADE,
        related_name="payments",
    )
