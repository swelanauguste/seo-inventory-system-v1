from django.contrib import admin

from .models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["supplier_name", "slug", "created_at", "updated_at"]
    prepopulated_fields = {
        "slug": ("supplier_name",),
    }