# Generated by Django 2.0.4 on 2018-05-04 21:11
from __future__ import annotations

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0042_auto_20180413_1933"),
        ("info", "0003_auto_20170218_1148"),
    ]

    operations = [
        migrations.AddField(
            model_name="infocategory",
            name="team",
            field=models.ForeignKey(
                blank=True,
                help_text="The team responsible for this info category.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="teams.Team",
            ),
        ),
    ]
