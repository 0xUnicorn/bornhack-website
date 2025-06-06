# Generated by Django 4.2.21 on 2025-05-29 05:03
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("maps", "0004_userlocationtype_userlocation"),
    ]

    operations = [
        migrations.AddField(
            model_name="layer",
            name="public",
            field=models.BooleanField(default=True, help_text="Make the layer visible to the public. A non-public layer is only visible for team members"),
        ),
    ]
