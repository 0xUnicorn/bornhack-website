# Generated by Django 4.2.5 on 2023-09-24 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("program", "0104_alter_speaker_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="url",
            name="event",
            field=models.ForeignKey(
                blank=True,
                help_text="The event proposal object this URL belongs to",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="urls",
                to="program.event",
            ),
        ),
        migrations.AlterField(
            model_name="url",
            name="event_proposal",
            field=models.ForeignKey(
                blank=True,
                help_text="The event proposal object this URL belongs to",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="urls",
                to="program.eventproposal",
            ),
        ),
        migrations.AlterField(
            model_name="url",
            name="speaker",
            field=models.ForeignKey(
                blank=True,
                help_text="The speaker proposal object this URL belongs to",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="urls",
                to="program.speaker",
            ),
        ),
        migrations.AlterField(
            model_name="url",
            name="speaker_proposal",
            field=models.ForeignKey(
                blank=True,
                help_text="The speaker proposal object this URL belongs to",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="urls",
                to="program.speakerproposal",
            ),
        ),
    ]
