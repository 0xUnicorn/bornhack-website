# Generated by Django 2.1.7 on 2019-07-11 18:37
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("rideshare", "0004_auto_20190711_2036"),
    ]

    operations = [
        migrations.AddField(
            model_name="ride",
            name="to_location",
            field=models.CharField(default="BornHack", max_length=100),
            preserve_default=False,
        ),
    ]
