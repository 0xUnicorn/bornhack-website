# Generated by Django 3.2.12 on 2022-04-02 13:56

from django.db import migrations


def backfill_refunds(apps, schema_editor):
    """Loop over Orders with refunded=True and create Refund and RefundProductRelation objects."""
    Order = apps.get_model("shop", "Order")
    Refund = apps.get_model("shop", "Refund")
    RefundProductRelation = apps.get_model("shop", "RefundProductRelation")

    for order in Order.objects.filter(refunded=True, refunds__isnull=True):
        refund = Refund.objects.create(
            order=order,
            notes="Auto-generated Refund from shop/migrations/0071_backfill_refunds.py",
        )
        for opr in order.oprs.all():
            RefundProductRelation.objects.create(
                refund=refund, opr=opr, quantity=opr.quantity
            )


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0070_fixup_opr"),
    ]

    operations = [
        migrations.RunPython(backfill_refunds),
    ]