# Generated by Django 1.10.5 on 2018-03-18 08:06
from __future__ import annotations

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("program", "0045_event_proposal")]

    operations = [
        migrations.AlterField(
            model_name="favorite",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="favorites",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
