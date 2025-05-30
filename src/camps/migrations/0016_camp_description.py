# Generated by Django 1.10.4 on 2017-01-16 16:37
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("camps", "0015_auto_20170116_1634")]

    operations = [
        migrations.AddField(
            model_name="camp",
            name="description",
            field=models.TextField(
                default=b"",
                help_text=b"Description of the camp, shown on the camp frontpage. HTML and markdown supported.",
                verbose_name=b"Description",
            ),
        ),
    ]
