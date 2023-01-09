from django.db import models
from django.contrib.auth.models import AbstractUser
from django_softdelete.models import SoftDeleteModel, SoftDeleteManager

import uuid

# Create your models here.


class User(AbstractUser, SoftDeleteModel, models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(unique=True, max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=13)
    is_seller = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
