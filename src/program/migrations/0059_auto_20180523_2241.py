# Generated by Django 2.0.4 on 2018-05-23 20:41
from __future__ import annotations

import uuid

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("program", "0058_auto_20180523_0844")]

    operations = [
        migrations.RemoveField(model_name="url", name="id"),
        migrations.AddField(
            model_name="url",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
