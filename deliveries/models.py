from django.db import models
import uuid


class Delivery(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    delivery = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    addresses = models.ForeignKey(
        "addresses.Address", on_delete=models.CASCADE, related_name="delivery"
    )
