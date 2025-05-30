# Generated by Django 2.1 on 2018-08-19 15:14
from __future__ import annotations

from django.db import migrations


def add_bogus_email(apps, schema_editor) -> None:
    Speaker = apps.get_model("program", "Speaker")

    for speaker in Speaker.objects.all():
        if not speaker.email:
            speaker.email = "N/A"
            speaker.save()


class Migration(migrations.Migration):
    dependencies = [("program", "0068_add_email_to_speaker_and_speaker_proposal")]

    operations = [migrations.RunPython(add_bogus_email)]
