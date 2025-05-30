# Generated by Django 1.10.5 on 2017-04-30 12:18
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OutgoingEmail",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("subject", models.CharField(max_length=500)),
                ("text_template", models.TextField()),
                ("html_template", models.TextField(blank=True)),
                ("recipient", models.CharField(max_length=500)),
                ("sender", models.CharField(max_length=500)),
                ("attachment", models.FileField(blank=True, upload_to="")),
                ("processed", models.BooleanField(default=False)),
            ],
            options={"abstract": False},
        ),
    ]
