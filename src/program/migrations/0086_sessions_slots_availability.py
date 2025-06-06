# Generated by Django 3.0.3 on 2020-04-12 18:17
from __future__ import annotations

import uuid

import django.contrib.postgres.constraints
import django.contrib.postgres.fields.ranges
import django.db.models.deletion
import django.db.models.expressions
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("camps", "0034_add_team_permission_sets"),
        ("program", "0085_btree_gist_extension"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventSession",
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
                (
                    "when",
                    django.contrib.postgres.fields.ranges.DateTimeRangeField(
                        help_text="A period of time where this type of event can be scheduled. Input format is <i>YYYY-MM-DD HH:MM</i>",
                    ),
                ),
                (
                    "event_duration_minutes",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="The duration of events in this EventSession. Defaults to the value from the EventType of this EventSession.",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Description of this session (optional).",
                    ),
                ),
            ],
            options={
                "ordering": ["when", "event_type", "event_location"],
            },
        ),
        migrations.CreateModel(
            name="EventSlot",
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
                (
                    "when",
                    django.contrib.postgres.fields.ranges.DateTimeRangeField(
                        help_text="Start and end time of this slot",
                    ),
                ),
                (
                    "autoscheduled",
                    models.NullBooleanField(
                        default=None,
                        help_text="True if the Event was scheduled by the AutoScheduler, False if it was scheduled manually, None if there is nothing scheduled in this EventSlot.",
                    ),
                ),
            ],
            options={
                "ordering": ["when"],
            },
        ),
        migrations.CreateModel(
            name="SpeakerAvailability",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "when",
                    django.contrib.postgres.fields.ranges.DateTimeRangeField(
                        db_index=True,
                        help_text="The period when this speaker is available or unavailable. Must be 1 hour!",
                    ),
                ),
                (
                    "available",
                    models.BooleanField(
                        db_index=True,
                        help_text="Is the speaker available or unavailable during this hour? Check for available, uncheck for unavailable.",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SpeakerEventConflict",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SpeakerProposalAvailability",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "when",
                    django.contrib.postgres.fields.ranges.DateTimeRangeField(
                        db_index=True,
                        help_text="The period when this speaker is available or unavailable. Must be 1 hour!",
                    ),
                ),
                (
                    "available",
                    models.BooleanField(
                        db_index=True,
                        help_text="Is the speaker available or unavailable during this hour? Check for available, uncheck for unavailable.",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SpeakerProposalEventConflict",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="event",
            name="demand",
            field=models.PositiveIntegerField(
                default=0,
                help_text="The estimated demand for this event. Used by the autoscheduler to pick the optimal location for events. Set to 0 to disable demand constraints for this event.",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="duration_minutes",
            field=models.PositiveIntegerField(
                null=True,
                blank=True,
                default=None,
                help_text="The duration of this event in minutes. Leave blank to use the default from the eventtype.",
            ),
        ),
        migrations.AddField(
            model_name="eventinstance",
            name="autoscheduled",
            field=models.BooleanField(
                default=False,
                help_text="True if this was created by the autoscheduler.",
            ),
        ),
        migrations.AddField(
            model_name="eventlocation",
            name="capacity",
            field=models.PositiveIntegerField(
                default=20,
                help_text="The capacity of this location. Used by the autoscheduler.",
            ),
        ),
        migrations.AddField(
            model_name="eventlocation",
            name="conflicts",
            field=models.ManyToManyField(
                help_text="Select the locations which this location conflicts with. Nothing can be scheduled in a location if a conflicting location has an EventInstance at the same time. Example: If one room can be split into two, then the big room would conflict with each of the two small rooms (but the small rooms would not conflict with eachother).",
                related_name="_eventlocation_conflicts_+",
                to="program.EventLocation",
            ),
        ),
        migrations.AddField(
            model_name="eventtype",
            name="event_duration_minutes",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="The default duration of an event of this type, in minutes. Optional. This default can be overridden in individual EventSessions as needed.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="eventtype",
            name="support_autoscheduling",
            field=models.BooleanField(
                default=False,
                help_text="Check to enable this EventType in the autoscheduler",
            ),
        ),
        migrations.AlterField(
            model_name="eventinstance",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="eventinstances",
                to="program.EventLocation",
            ),
        ),
        migrations.AlterField(
            model_name="eventinstance",
            name="when",
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(
                blank=True,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="eventproposal",
            name="event_type",
            field=models.ForeignKey(
                help_text="The type of event",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="eventproposals",
                to="program.EventType",
            ),
        ),
        migrations.AddConstraint(
            model_name="eventinstance",
            constraint=django.contrib.postgres.constraints.ExclusionConstraint(
                expressions=[("when", "&&"), ("location", "=")],
                name="prevent_eventinstance_location_overlaps",
            ),
        ),
        migrations.AddField(
            model_name="speakerproposaleventconflict",
            name="events",
            field=models.ManyToManyField(
                help_text="The conflict events",
                related_name="speakerproposalconflicts",
                to="program.Event",
            ),
        ),
        migrations.AddField(
            model_name="speakerproposaleventconflict",
            name="speakerproposal",
            field=models.OneToOneField(
                help_text="The SpeakerProposal",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="eventconflicts",
                to="program.SpeakerProposal",
            ),
        ),
        migrations.AddField(
            model_name="speakerproposalavailability",
            name="speakerproposal",
            field=models.ForeignKey(
                blank=True,
                help_text="The speaker proposal object this availability belongs to",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="availabilities",
                to="program.SpeakerProposal",
            ),
        ),
        migrations.AddField(
            model_name="speakereventconflict",
            name="events",
            field=models.ManyToManyField(
                help_text="The conflict events",
                related_name="speakerconflicts",
                to="program.Event",
            ),
        ),
        migrations.AddField(
            model_name="speakereventconflict",
            name="speaker",
            field=models.OneToOneField(
                help_text="The Speaker",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="eventconflicts",
                to="program.Speaker",
            ),
        ),
        migrations.AddField(
            model_name="speakeravailability",
            name="speaker",
            field=models.ForeignKey(
                blank=True,
                help_text="The speaker object this availability belongs to (if any)",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="availabilities",
                to="program.Speaker",
            ),
        ),
        migrations.AddField(
            model_name="eventslot",
            name="event",
            field=models.ForeignKey(
                blank=True,
                help_text="The Event scheduled in this EventSlot",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="event_slots",
                to="program.Event",
            ),
        ),
        migrations.AddField(
            model_name="eventslot",
            name="event_session",
            field=models.ForeignKey(
                help_text="The EventSession this EventSlot belongs to",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="event_slots",
                to="program.EventSession",
            ),
        ),
        migrations.AddField(
            model_name="eventsession",
            name="camp",
            field=models.ForeignKey(
                help_text="The Camp this EventSession belongs to",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="eventsessions",
                to="camps.Camp",
            ),
        ),
        migrations.AddField(
            model_name="eventsession",
            name="event_location",
            field=models.ForeignKey(
                help_text="The event location this session is for",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="eventsessions",
                to="program.EventLocation",
            ),
        ),
        migrations.AddField(
            model_name="eventsession",
            name="event_type",
            field=models.ForeignKey(
                help_text="The type of event this session is for",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="eventsessions",
                to="program.EventType",
            ),
        ),
        migrations.AddConstraint(
            model_name="speakerproposalavailability",
            constraint=django.contrib.postgres.constraints.ExclusionConstraint(
                expressions=[
                    (django.db.models.expressions.F("speakerproposal"), "="),
                    ("when", "&&"),
                ],
                name="prevent_speakerproposalavailability_overlaps",
            ),
        ),
        migrations.AddConstraint(
            model_name="speakeravailability",
            constraint=django.contrib.postgres.constraints.ExclusionConstraint(
                expressions=[
                    (django.db.models.expressions.F("speaker"), "="),
                    ("when", "&&"),
                ],
                name="prevent_speakeravailability_overlaps",
            ),
        ),
        migrations.AddConstraint(
            model_name="eventslot",
            constraint=django.contrib.postgres.constraints.ExclusionConstraint(
                expressions=[("when", "&&"), ("event_session", "=")],
                name="prevent_slot_session_overlaps",
            ),
        ),
        migrations.AddConstraint(
            model_name="eventsession",
            constraint=django.contrib.postgres.constraints.ExclusionConstraint(
                expressions=[
                    ("when", "&&"),
                    ("event_location", "="),
                    ("event_type", "="),
                ],
                name="prevent_eventsession_eventtype_eventlocation_overlaps",
            ),
        ),
    ]
