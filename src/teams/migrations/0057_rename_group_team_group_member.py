# Generated by Django 4.2.21 on 2025-06-08 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0056_alter_team_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='group',
            new_name='group_member',
        ),
    ]
