from django.db import models

# Create your models here.
class Category_product(models.Model):
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
