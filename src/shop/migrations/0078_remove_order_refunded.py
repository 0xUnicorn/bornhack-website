# Generated by Django 3.2.14 on 2022-07-18 09:11
from __future__ import annotations

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0077_refund_created_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="refunded",
        ),
    ]
