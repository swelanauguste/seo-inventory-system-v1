from django.contrib import admin

from .models import Supplier, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at", "updated_at"]
    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["supplier_name", "slug", "created_at", "updated_at"]
    prepopulated_fields = {
        "slug": ("supplier_name",),
    }