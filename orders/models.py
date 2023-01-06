from django.db import models
import uuid

# Create your models here.


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )

    delivery = models.ForeignKey(
        "deliveries.Delivery", on_delete=models.CASCADE, related_name="orders"
    )
