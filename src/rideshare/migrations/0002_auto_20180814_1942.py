# Generated by Django 2.1 on 2018-08-14 17:42
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("rideshare", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="ride",
            name="when",
            field=models.DateTimeField(help_text="Format is YYYY-MM-DD HH:mm"),
        ),
    ]
