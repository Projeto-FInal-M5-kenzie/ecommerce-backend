# Generated by Django 4.1.4 on 2023-01-06 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("payments", "0001_initial"),
        ("carts", "0001_initial"),
        ("deliveries", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="carts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="delivery",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="carts",
                to="deliveries.delivery",
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="payment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="carts",
                to="payments.payment",
            ),
        ),
    ]
