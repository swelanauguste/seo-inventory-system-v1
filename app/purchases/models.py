from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from mixins.assets import TimeStampMixin
from suppliers.models import Supplier


class Bill(TimeStampMixin):
    """
    Bill model
    """

    purchase_order_number = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    supplier = models.ForeignKey(
        Supplier, related_name="bills", on_delete=models.CASCADE
    )
    file = models.FileField(upload_to="purchases/bills/")
    total = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.purchase_order_number

    def save(self, *args, **kwargs):
        self.slug = slugify(self.purchase_order_number)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("purchases:detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("purchases:update", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-created_at"]


# class Product(TimeStampMixin):
#     """Product model"""

#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, unique=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()
#     bill = models.ForeignKey(Bill, related_name="products", on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse("purchases:product-detail", kwargs={"slug": self.slug})

#     class Meta:
#         ordering = ["-created_at"]
