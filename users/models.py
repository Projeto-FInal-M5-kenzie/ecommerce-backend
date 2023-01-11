from django.db import models
from django.contrib.auth.models import AbstractUser
from django_softdelete.models import SoftDeleteModel, SoftDeleteManager
from django.dispatch import receiver
from .utils import send_account_activation_email
from django.db.models.signals import post_save
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
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=150, null=True, blank=True)


@receiver(post_save, sender=User)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if created:
            email_token = instance.email_token
            email = instance.email
            send_account_activation_email(email=email, email_token=email_token)
    except Exception as error:
        print(error)
