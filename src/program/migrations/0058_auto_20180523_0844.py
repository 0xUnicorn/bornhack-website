# Generated by Django 2.0.4 on 2018-05-23 06:44
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("program", "0057_auto_20180522_0659")]

    operations = [
        migrations.AlterModelOptions(name="urltype", options={"ordering": ["name"]}),
        migrations.AlterField(
            model_name="urltype",
            name="name",
            field=models.CharField(
                help_text="The name of this type",
                max_length=25,
                unique=True,
            ),
        ),
    ]
