from django.contrib import admin

from .models import Bill

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ["purchase_order_number", "slug", "created_at", "updated_at"]
    prepopulated_fields = {
        "slug": ("purchase_order_number",),
    }
