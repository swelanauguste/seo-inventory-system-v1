from django.contrib import admin

from .models import Department, Position, Staff

admin.site.register(Staff)
admin.site.register(Position)
admin.site.register(Department)
