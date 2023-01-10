from django.db import models
import uuid
from django_softdelete.models import SoftDeleteModel, SoftDeleteManager

# Create your models here.
class Category_product(SoftDeleteModel, models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, editable=False)
    deleted_at = models.DateTimeField(blank=True,  null=True)
    undeleted_objects = SoftDeleteManager()
    all_objects = models.Manager()