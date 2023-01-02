from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Seller(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    company_name = models.CharField(max_length=150, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    client = models.OneToOneField(
        "clients.Client",
        on_delete=models.CASCADE,
        related_name="seller",
    )
