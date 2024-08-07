# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-13 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("teams", "0041_auto_20180412_2231")]

    operations = [
        migrations.AddField(
            model_name="team",
            name="private_irc_channel_fix_needed",
            field=models.BooleanField(
                default=False,
                help_text="Used to indicate to the IRC bot that this teams private IRC channel is in need of a permissions and ACL fix.",
            ),
        ),
        migrations.AddField(
            model_name="team",
            name="public_irc_channel_fix_needed",
            field=models.BooleanField(
                default=False,
                help_text="Used to indicate to the IRC bot that this teams public IRC channel is in need of a permissions and ACL fix.",
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="public_irc_channel_managed",
            field=models.BooleanField(
                default=False,
                help_text="Check to make the bot manage the teams public IRC channel by registering it with NickServ and setting +Oo for all teammembers.",
            ),
        ),
    ]
