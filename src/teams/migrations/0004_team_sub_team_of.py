# Generated by Django 1.10.5 on 2017-04-01 20:32
from __future__ import annotations

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("teams", "0003_auto_20170401_2227")]

    operations = [
        migrations.AddField(
            model_name="team",
            name="sub_team_of",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="teams.Team",
            ),
        ),
    ]
