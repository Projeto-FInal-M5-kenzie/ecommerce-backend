# Generated by Django 4.1 on 2023-01-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_otp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="otp",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
