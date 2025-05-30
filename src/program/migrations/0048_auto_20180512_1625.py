# Generated by Django 2.0.4 on 2018-05-12 14:25
from __future__ import annotations

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("camps", "0026_auto_20180506_1633"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("program", "0047_auto_20180415_1159"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventTrack",
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
                (
                    "camp",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="eventtracks",
                        to="camps.Camp",
                    ),
                ),
                (
                    "managers",
                    models.ManyToManyField(
                        related_name="managed_tracks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(model_name="speaker", name="picture_large"),
        migrations.RemoveField(model_name="speaker", name="picture_small"),
        migrations.RemoveField(model_name="speakerproposal", name="picture_large"),
        migrations.RemoveField(model_name="speakerproposal", name="picture_small"),
        migrations.AddField(
            model_name="eventproposal",
            name="duration",
            field=models.IntegerField(
                blank=True,
                default=None,
                help_text="How much time (in minutes) should we set aside for this act? Please keep it between 60 and 180 minutes (1-3 hours).",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="eventtype",
            name="description",
            field=models.TextField(
                blank=True,
                default="",
                help_text="The description of this type of event. Used in content submission flow.",
            ),
        ),
        migrations.AddField(
            model_name="eventtype",
            name="icon",
            field=models.CharField(
                default="wrench",
                help_text="Name of the fontawesome icon to use, without the 'fa-' part",
                max_length=25,
            ),
        ),
        migrations.AddField(
            model_name="eventtype",
            name="oneday_ticket_possible",
            field=models.BooleanField(
                default=False,
                help_text="Check if hosting an event of this type qualifies someone for a free oneday ticket",
            ),
        ),
        migrations.AddField(
            model_name="speaker",
            name="needs_oneday_ticket",
            field=models.BooleanField(
                default=False,
                help_text="Check if BornHack needs to provide a free one-day ticket for this speaker",
            ),
        ),
        migrations.AddField(
            model_name="speakerproposal",
            name="needs_oneday_ticket",
            field=models.BooleanField(
                default=False,
                help_text="Check if BornHack needs to provide a free one-day ticket for this speaker",
            ),
        ),
        migrations.AlterField(
            model_name="eventlocation",
            name="icon",
            field=models.CharField(
                help_text="Name of the fontawesome icon to use without the 'fa-' part",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="eventproposal",
            name="abstract",
            field=models.TextField(
                blank=True,
                help_text="The abstract for this event. Describe what the audience can expect to see/hear.",
            ),
        ),
        migrations.AlterField(
            model_name="eventproposal",
            name="proposal_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending approval"),
                    ("approved", "Approved"),
                    ("rejected", "Rejected"),
                ],
                default="pending",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="eventproposal",
            name="speakers",
            field=models.ManyToManyField(
                blank=True,
                help_text="Pick the speaker(s) for this event. If you cannot see anything here you need to go back and create Speaker Proposal(s) first.",
                related_name="eventproposals",
                to="program.SpeakerProposal",
            ),
        ),
        migrations.AlterField(
            model_name="eventproposal",
            name="title",
            field=models.CharField(
                help_text="The title of this event. Keep it short and memorable.",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="speakerproposal",
            name="biography",
            field=models.TextField(
                help_text="Biography of the speaker/artist/host. Markdown is supported.",
            ),
        ),
        migrations.AlterField(
            model_name="speakerproposal",
            name="name",
            field=models.CharField(
                help_text="Name or alias of the speaker/artist/host",
                max_length=150,
            ),
        ),
        migrations.AlterField(
            model_name="speakerproposal",
            name="proposal_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending approval"),
                    ("approved", "Approved"),
                    ("rejected", "Rejected"),
                ],
                default="pending",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="speakerproposal",
            name="submission_notes",
            field=models.TextField(
                blank=True,
                help_text="Private notes for this speaker/artist/host. Only visible to the submitting user and the BornHack organisers.",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="track",
            field=models.ForeignKey(
                blank=True,
                help_text="The track this event belongs to",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="events",
                to="program.EventTrack",
            ),
        ),
        migrations.AddField(
            model_name="eventproposal",
            name="track",
            field=models.ForeignKey(
                blank=True,
                help_text="The track this event belongs to",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="eventproposals",
                to="program.EventTrack",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="eventtrack",
            unique_together={("camp", "slug"), ("camp", "name")},
        ),
    ]
