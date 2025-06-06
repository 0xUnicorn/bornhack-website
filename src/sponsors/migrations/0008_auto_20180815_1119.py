# Generated by Django 2.1 on 2018-08-15 09:19
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("sponsors", "0007_auto_20180318_0906")]

    operations = [
        migrations.AddField(
            model_name="sponsor",
            name="tickets_generated",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="sponsortier",
            name="tickets",
            field=models.IntegerField(
                blank=True,
                help_text="If set this is the number of tickets generated for a sponsor in this tier.",
                null=True,
            ),
        ),
    ]
