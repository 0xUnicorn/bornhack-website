# Generated by Django 1.10.4 on 2016-12-29 21:50
from __future__ import annotations

import django.contrib.postgres.fields.ranges
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("program", "0011_auto_20161229_2149")]

    operations = [
        migrations.AlterField(
            model_name="eventinstance",
            name="when",
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(),
        ),
    ]
