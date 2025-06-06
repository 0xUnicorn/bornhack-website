# Generated by Django 3.0.3 on 2020-06-17 15:48
from __future__ import annotations

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
import django.contrib.postgres.constraints
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("facilities", "0006_auto_20200616_2330"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="facilityopeninghours",
            options={"ordering": ["when"]},
        ),
        migrations.AlterField(
            model_name="facility",
            name="location",
            field=django.contrib.gis.db.models.fields.PointField(
                default=django.contrib.gis.geos.point.Point(9.93891, 55.38562),
                help_text="The location of this facility.",
                srid=4326,
            ),
        ),
        migrations.AddConstraint(
            model_name="facilityopeninghours",
            constraint=django.contrib.postgres.constraints.ExclusionConstraint(
                expressions=[("when", "&&"), ("facility", "=")],
                name="prevent_facility_opening_hours_overlaps",
            ),
        ),
    ]
