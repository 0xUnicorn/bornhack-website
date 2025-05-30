# Generated by Django 3.2.5 on 2021-08-02 17:56
from __future__ import annotations

from django.db import migrations


def populate_ticket_used_when(apps, schema_editor) -> None:
    ShopTicket = apps.get_model("tickets", "ShopTicket")
    SponsorTicket = apps.get_model("tickets", "SponsorTicket")
    DiscountTicket = apps.get_model("tickets", "DiscountTicket")

    for st in ShopTicket.objects.filter(used_time__isnull=True, used=True):
        st.used_when = st.updated
        st.save()

    for st in SponsorTicket.objects.filter(used_time__isnull=True, used=True):
        st.used_when = st.updated
        st.save()

    for _dt in DiscountTicket.objects.filter(used_time__isnull=True, used=True):
        st.used_when = st.updated
        st.save()


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0019_auto_20210802_1756"),
    ]

    operations = [migrations.RunPython(populate_ticket_used_when)]
