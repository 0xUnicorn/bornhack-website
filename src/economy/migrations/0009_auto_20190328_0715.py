# Generated by Django 2.1.7 on 2019-03-28 06:15
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("economy", "0008_auto_20190327_1721")]

    operations = [
        migrations.AlterField(
            model_name="chain",
            name="slug",
            field=models.SlugField(
                blank=True,
                help_text="The url slug for this Chain. Leave blank to auto generate a slug.",
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="credebtor",
            name="slug",
            field=models.SlugField(
                blank=True,
                help_text="The url slug for this Credebtor. Leave blank to auto generate a slug.",
            ),
        ),
    ]
