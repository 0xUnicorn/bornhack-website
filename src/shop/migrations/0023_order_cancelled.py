# Generated by Django 1.9.6 on 2016-06-01 08:53
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("shop", "0022_auto_20160530_2301")]

    operations = [
        migrations.AddField(
            model_name="order",
            name="cancelled",
            field=models.BooleanField(default=False),
        ),
    ]
