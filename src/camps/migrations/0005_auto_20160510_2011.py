# Generated by Django 1.9.6 on 2016-05-10 20:11
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("camps", "0004_camp_ticket_sale_open")]

    operations = [
        migrations.RemoveField(model_name="camp", name="ticket_sale_open"),
        migrations.AddField(
            model_name="camp",
            name="shop_open",
            field=models.BooleanField(
                default=False,
                help_text="Whether the shop is open or not.",
                verbose_name="Shop open?",
            ),
        ),
    ]
