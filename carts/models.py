from django.db import models
import uuid

# Create your models here.
class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    subtotal_price = models.DecimalField(max_digits=8, decimal_places=2)
    frete = models.DecimalField(max_digits=8, decimal_places=2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    client = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="carts")
    delivery = models.ForeignKey("deliveries.Delivery", on_delete=models.CASCADE, related_name="carts")
    payment = models.ForeignKey("payments.Payment", on_delete=models.CASCADE, related_name="carts", default="")
    product = models.ForeignKey("products.OrderProduct", on_delete=models.CASCADE, related_name="carts")