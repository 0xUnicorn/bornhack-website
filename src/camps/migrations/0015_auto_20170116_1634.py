# Generated by Django 1.10.4 on 2017-01-16 16:34
from __future__ import annotations

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("camps", "0014_auto_20161229_2202")]

    operations = [
        migrations.RemoveField(model_name="expense", name="refund_user"),
        migrations.DeleteModel(name="Expense"),
    ]
