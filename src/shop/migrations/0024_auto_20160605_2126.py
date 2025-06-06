# Generated by Django 1.9.2 on 2016-06-05 21:26
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("shop", "0023_order_cancelled")]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["available_in", "price"],
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.AlterField(
            model_name="order",
            name="payment_method",
            field=models.CharField(
                choices=[
                    (b"credit_card", b"Credit card"),
                    (b"blockchain", b"Blockchain"),
                    (b"bank_transfer", b"Bank transfer"),
                ],
                default=b"",
                max_length=50,
            ),
        ),
    ]
