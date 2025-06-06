# Generated by Django 4.2.16 on 2024-10-01 19:22
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0011_alter_profile_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="theme",
            field=models.CharField(
                choices=[("default", "Default (Auto)"), ("slate", "Slate"), ("solar", "Solar")],
                default="default",
                max_length=20,
            ),
        ),
    ]
