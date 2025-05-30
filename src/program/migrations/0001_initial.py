# Generated by Django 1.9.6 on 2016-07-13 19:38
from __future__ import annotations

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [("camps", "0005_auto_20160510_2011")]

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("start", models.TimeField()),
                ("end", models.TimeField()),
                ("days", models.ManyToManyField(to="camps.Day")),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="EventType",
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
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField()),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Speaker",
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
                ("name", models.CharField(max_length=150)),
                ("biography", models.TextField()),
                ("picture", models.ImageField(blank=True, null=True, upload_to=b"")),
                (
                    "events",
                    models.ManyToManyField(
                        related_name="speakers",
                        related_query_name="speaker",
                        to="program.Event",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="event",
            name="event_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="program.EventType",
            ),
        ),
    ]
