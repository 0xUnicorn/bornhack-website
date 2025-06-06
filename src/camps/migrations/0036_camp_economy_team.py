# Generated by Django 3.2.7 on 2021-09-02 10:06
from __future__ import annotations

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0052_team_permission_set"),
        ("camps", "0035_add_gameteam_permissionset"),
    ]

    operations = [
        migrations.AddField(
            model_name="camp",
            name="economy_team",
            field=models.ForeignKey(
                blank=True,
                help_text="The economy team for this camp.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="teams.team",
            ),
        ),
    ]
