from django.db import models
import uuid

# Create your models here.


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name_product = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    price = models.FloatField(2, null=True)
    stock = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    quantity = models.IntegerField(default=1)

    sellers = models.ManyToManyField("sellers.Seller", related_name="products")

    category = models.ForeignKey(
        "categories_products.Category_product",
        on_delete=models.CASCADE,
        related_name="products",
    )

    orders = models.ManyToManyField(
        "orders.Order",
        through="products.OrderProduct",
        related_name="order_products",
    )


class OrderProduct(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )


# class OrderProduct(models.Model):
#     id = models.UUIDField(
#         default=uuid.uuid4,
#         primary_key=True,
#         editable=False,
#     )
#     quantity_product = models.IntegerField(null=True)
#     subtotal_price = models.FloatField(2, null=True)
#     total_price = models.FloatField(2, null=True)
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     updated_at = models.DateTimeField(auto_now_add=True, editable=False)

#     clients = models.ForeignKey(
#         "users.User", on_delete=models.CASCADE, related_name="orders"
#     )
#     products = models.ForeignKey(
#         "products.Product", on_delete=models.CASCADE, related_name="orders"
#     )

#     cart = models.ForeignKey(
#         "carts.Cart", on_delete=models.CASCADE, related_name="products"
#     )
