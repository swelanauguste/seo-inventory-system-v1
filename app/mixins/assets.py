from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

DISTRICT_LIST = [
    ("Gros Islet", "Gros Islet"),
    ("Castries", "Castries"),
    ("Soufriere", "Soufriere"),
    ("Vieux Fort", "Vieux Fort"),
]

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="%(class)s_created",
        default=1,
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="%(class)s_updated",
        default=1,
    )

    class Meta:
        abstract = True

