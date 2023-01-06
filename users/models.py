from django.db import models
from django.contrib.auth.models import AbstractUser 
import uuid

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(unique=True, max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    payment = models.OneToOneField("payments.Payment", on_delete=models.CASCADE)

