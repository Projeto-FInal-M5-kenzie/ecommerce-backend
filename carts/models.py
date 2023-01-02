from django.db import models

# Create your models here.
class Cart(models.Model):
    subtotal_price = models.DecimalField(max_digits=8, decimal_places=2)
    frete = models.DecimalField(max_digits=8, decimal_places=2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE, related_name="carts")
    