# Generated by Django 2.1 on 2018-08-22 13:18
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("shop", "0054_auto_20180415_1159")]

    operations = [
        migrations.AddField(
            model_name="order",
            name="customer_address",
            field=models.TextField(
                blank=True,
                help_text="The additional customer address for this order",
            ),
        ),
    ]
