# Generated by Django 1.10.5 on 2017-05-07 13:41
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("shop", "0043_auto_20170507_1309")]

    operations = [
        migrations.AddField(
            model_name="coinifyapiinvoice",
            name="coinify_id",
            field=models.IntegerField(null=True),
        ),
    ]
