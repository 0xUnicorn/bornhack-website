# Generated by Django 4.2.16 on 2024-09-28 06:10
from __future__ import annotations

from django.contrib.auth.models import Group
from django.db import migrations


def create_team_groups(apps, schema_editor) -> None:
    Team = apps.get_model("teams", "Team")

    for team in Team.objects.all():
        # skip team if it already has a group
        if hasattr(team, "group"):
            continue
        # get or create group for team
        group, created = Group.objects.get_or_create(
            name=f"{team.camp.slug}-{team.slug}-team",
        )
        # set group and save
        team.group = group
        team.save()
        # loop over team memberships and add group memberships
        for membership in team.memberships.all():
            membership.update_group_memberships()


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0053_alter_teammember_options_and_more"),
    ]

    operations = [
        migrations.RunPython(create_team_groups),
    ]
