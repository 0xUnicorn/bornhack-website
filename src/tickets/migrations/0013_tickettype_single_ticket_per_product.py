# Generated by Django 2.2.3 on 2019-07-30 20:49
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0012_auto_20190724_2037"),
    ]

    operations = [
        migrations.AddField(
            model_name="tickettype",
            name="single_ticket_per_product",
            field=models.BooleanField(
                default=False,
                help_text="Only create one ticket for a product/order pair no matter the quantity. Useful for products which are bought in larger quantity (ie. village chairs)",
            ),
        ),
    ]
