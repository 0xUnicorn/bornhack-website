# Generated by Django 3.2.7 on 2021-09-09 13:05
from __future__ import annotations

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("economy", "0025_clearhaussettlement"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="clearhaussettlement",
            options={
                "get_latest_by": ["period_start_date"],
                "ordering": ["-period_start_date"],
            },
        ),
    ]
