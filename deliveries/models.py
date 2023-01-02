from django.db import models

class Delivery(models.Model):
    delivery = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    addresses = models.ForeignKey(
        "addresses.Address", on_delete=models.CASCADE, related_name="delivery"
    )
    