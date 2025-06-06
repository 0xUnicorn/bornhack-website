# Generated by Django 2.0.4 on 2018-08-29 22:14
from __future__ import annotations

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("teams", "0049_auto_20180815_1119"),
        ("camps", "0031_auto_20180830_0014"),
    ]

    operations = [
        migrations.CreateModel(
            name="Expense",
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
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="The amount of this expense in DKK. Must match the amount on the invoice uploaded below.",
                        max_digits=12,
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="A short description of this expense. Please keep it meningful as it helps the Economy team a lot when categorising expenses. 200 characters or fewer.",
                        max_length=200,
                    ),
                ),
                (
                    "paid_by_bornhack",
                    models.BooleanField(
                        default=True,
                        help_text="Leave checked if this expense was paid by BornHack. Uncheck if you need a reimbursement for this expense.",
                    ),
                ),
                (
                    "invoice",
                    models.ImageField(
                        help_text="The invoice for this expense. Please make sure the amount on the invoice matches the amount you entered above. All common image formats are accepted.",
                        upload_to="expenses/",
                    ),
                ),
                (
                    "approved",
                    models.NullBooleanField(
                        default=None,
                        help_text="True if this expense has been approved by the responsible team. False if it has been rejected. Blank if noone has decided yet.",
                    ),
                ),
                (
                    "notes",
                    models.TextField(
                        blank=True,
                        help_text="Economy Team notes for this expense. Only visible to the Economy team and the submitting user.",
                    ),
                ),
                (
                    "camp",
                    models.ForeignKey(
                        help_text="The camp to which this expense belongs",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="expenses",
                        to="camps.Camp",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Reimbursement",
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
                    "notes",
                    models.TextField(
                        blank=True,
                        help_text="Economy Team notes for this reimbursement. Only visible to the Economy team and the related user.",
                    ),
                ),
                (
                    "paid",
                    models.BooleanField(
                        default=False,
                        help_text="Check when this reimbursement has been paid to the user",
                    ),
                ),
                (
                    "camp",
                    models.ForeignKey(
                        help_text="The camp to which this reimbursement belongs",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reimbursements",
                        to="camps.Camp",
                    ),
                ),
                (
                    "reimbursement_user",
                    models.ForeignKey(
                        help_text="The user this reimbursement belongs to.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reimbursements",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user who created this reimbursement.",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_reimbursements",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="expense",
            name="reimbursement",
            field=models.ForeignKey(
                blank=True,
                help_text="The reimbursement for this expense, if any. This is a dual-purpose field. If expense.paid_by_bornhack is true then expense.reimbursement references the reimbursement which this expense is created to cover. If expense.paid_by_bornhack is false then expense.reimbursement references the reimbursement which reimbursed this expense.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="expenses",
                to="economy.Reimbursement",
            ),
        ),
        migrations.AddField(
            model_name="expense",
            name="responsible_team",
            field=models.ForeignKey(
                help_text="The team to which this Expense belongs. A team responsible will need to approve the expense. When in doubt pick the Economy team.",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="expenses",
                to="teams.Team",
            ),
        ),
        migrations.AddField(
            model_name="expense",
            name="user",
            field=models.ForeignKey(
                help_text="The user to which this expense belongs",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="expenses",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
