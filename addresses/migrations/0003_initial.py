# Generated by Django 4.1 on 2023-01-12 03:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("addresses", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="users",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="addresses",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
