# Generated by Django 2.1.7 on 2019-03-30 09:45
from __future__ import annotations

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("economy", "0009_auto_20190328_0715")]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="creditor",
            field=models.ForeignKey(
                help_text="The Creditor to which this expense belongs",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="expenses",
                to="economy.Credebtor",
            ),
        ),
        migrations.AlterField(
            model_name="revenue",
            name="debtor",
            field=models.ForeignKey(
                help_text="The Debtor to which this revenue belongs",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="revenues",
                to="economy.Credebtor",
            ),
        ),
    ]
