# Generated by Django 2.0.4 on 2018-05-19 21:25
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("program", "0052_auto_20180519_2324")]

    operations = [
        migrations.AlterField(
            model_name="eventproposal",
            name="allow_video_recording",
            field=models.BooleanField(
                default=False,
                help_text="Check to allow video recording of the event. Leave unchecked to avoid video recording.",
            ),
        ),
    ]
