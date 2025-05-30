# Generated by Django 1.10.5 on 2017-04-13 12:42
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("profiles", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="description",
            field=models.TextField(
                default="",
                help_text="Please include any info you think could be relevant, like drivers license, first aid certificates, crafts, skills and previous experience.",
            ),
        ),
    ]
