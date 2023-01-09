from django.db import models
import uuid

class Address(models.Model):
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.IntegerField()
    district = models.CharField(max_length=150)
    number = models.IntegerField()
    complement = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    users = models.ManyToManyField(
        "users.User", related_name="addresses"
    )
