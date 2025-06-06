# Generated by Django 1.9.6 on 2016-05-15 16:15
from __future__ import annotations

from django.db import migrations


def ensure_slugs(apps, schema_editor) -> None:
    ProductCategory = apps.get_model("shop", "ProductCategory")
    Product = apps.get_model("shop", "Product")

    for category in ProductCategory.objects.all():
        category.save()

    for product in Product.objects.all():
        product.save()


class Migration(migrations.Migration):
    dependencies = [("shop", "0005_product_slug")]

    operations = [migrations.RunPython(ensure_slugs, migrations.RunPython.noop)]
