from __future__ import annotations

from django.contrib import admin

from .models import Wish


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    pass
