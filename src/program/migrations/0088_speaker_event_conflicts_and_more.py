# Generated by Django 3.0.3 on 2020-04-20 22:59
from __future__ import annotations

import django.contrib.postgres.constraints
import django.db.models.deletion
from django.db import migrations
from django.db import models

import utils.database


class Migration(migrations.Migration):
    dependencies = [
        ("program", "0087_fk_and_related_name_underscores"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="speakereventconflict",
            name="events",
        ),
        migrations.RemoveField(
            model_name="speakereventconflict",
            name="speaker",
        ),
        migrations.RemoveField(
            model_name="speakerproposaleventconflict",
            name="events",
        ),
        migrations.RemoveField(
            model_name="speakerproposaleventconflict",
            name="speaker_proposal",
        ),
        migrations.AddField(
            model_name="eventtype",
            name="support_speaker_event_conflicts",
            field=models.BooleanField(
                default=True,
                help_text="True if Events of this type should be selectable in the EventConflict m2m for SpeakerProposal and Speaker objects.",
            ),
        ),
        migrations.AddField(
            model_name="speaker",
            name="event_conflicts",
            field=models.ManyToManyField(
                help_text="The Events this person wishes to attend. The AutoScheduler will avoid conflicts.",
                related_name="speaker_conflicts",
                to="program.Event",
            ),
        ),
        migrations.AddField(
            model_name="speakerproposal",
            name="event_conflicts",
            field=models.ManyToManyField(
                help_text="Pick the Events this person wishes to attend, and we will attempt to avoid scheduling conflicts.",
                related_name="speaker_proposal_conflicts",
                to="program.Event",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="event_type",
            field=models.ForeignKey(
                help_text="The type of this event",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="events",
                to="program.EventType",
            ),
        ),
        migrations.AlterField(
            model_name="eventlocation",
            name="conflicts",
            field=models.ManyToManyField(
                blank=True,
                help_text="Select the locations which this location conflicts with. Nothing can be scheduled in a location if a conflicting location has a scheduled Event at the same time. Example: If one room can be split into two, then the big room would conflict with each of the two small rooms (but the small rooms would not conflict with eachother).",
                related_name="_eventlocation_conflicts_+",
                to="program.EventLocation",
            ),
        ),
        migrations.AlterField(
            model_name="eventproposal",
            name="duration",
            field=models.IntegerField(
                blank=True,
                null=True,
                help_text="How much time (in minutes) should we set aside for this act? Please keep it between 60 and 180 minutes (1-3 hours).",
            ),
        ),
        migrations.AlterField(
            model_name="eventslot",
            name="event",
            field=models.ForeignKey(
                blank=True,
                help_text="The Event scheduled in this EventSlot",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="event_slots",
                to="program.Event",
            ),
        ),
        migrations.AddConstraint(
            model_name="speakeravailability",
            constraint=django.contrib.postgres.constraints.ExclusionConstraint(
                expressions=[
                    ("speaker", "="),
                    (utils.database.CastToInteger("available"), "="),
                    ("when", "-|-"),
                ],
                name="prevent_speaker_availability_adjacent_mergeable",
            ),
        ),
        migrations.AddConstraint(
            model_name="speakerproposalavailability",
            constraint=django.contrib.postgres.constraints.ExclusionConstraint(
                expressions=[
                    ("speaker_proposal", "="),
                    (utils.database.CastToInteger("available"), "="),
                    ("when", "-|-"),
                ],
                name="prevent_speaker_proposal_availability_adjacent_mergeable",
            ),
        ),
        migrations.DeleteModel(
            name="SpeakerEventConflict",
        ),
        migrations.DeleteModel(
            name="SpeakerProposalEventConflict",
        ),
    ]
