# Generated by Django 3.0.3 on 2020-04-12 18:15
from __future__ import annotations

from django.contrib.postgres.operations import BtreeGistExtension
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("program", "0084_auto_20200229_1801"),
    ]

    operations = [
        BtreeGistExtension(),
    ]
