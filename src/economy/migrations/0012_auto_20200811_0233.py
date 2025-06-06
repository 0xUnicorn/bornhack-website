# Generated by Django 3.1 on 2020-08-11 00:33
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("economy", "0011_pos_posreport"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="approved",
            field=models.BooleanField(
                default=None,
                help_text="True if this expense has been approved by the responsible team. False if it has been rejected. Blank if noone has decided yet.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="revenue",
            name="approved",
            field=models.BooleanField(
                default=None,
                help_text="True if this Revenue has been approved by the responsible team. False if it has been rejected. Blank if noone has decided yet.",
                null=True,
            ),
        ),
    ]
