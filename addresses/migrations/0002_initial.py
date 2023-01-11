# Generated by Django 4.1 on 2023-01-11 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("addresses", "0001_initial"),
        ("sellers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="seller",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Addresses",
                to="sellers.seller",
            ),
        ),
    ]
