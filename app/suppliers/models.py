from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from mixins.assets import DISTRICT_LIST, TimeStampMixin


class Supplier(TimeStampMixin):
    supplier_name = models.CharField("supplier's name", max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    district = models.CharField(
        max_length=25, choices=DISTRICT_LIST, default="Castries"
    )
    website = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    tags = models.TextField(
        blank=True, null=True, help_text="Tags separated by comma eg.: #tag, #tags"
    )

    # objects = models.Manager()
    # object_list = IsNotDeletedManager()

    class Meta:
        ordering = ["-supplier_name"]

    # def get_delete_url(self):
    #     return reverse("suppliers:supplier-delete", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("suppliers:update", kwargs={"slug": self.slug})

    def get_absolute_url(self):
        return reverse("suppliers:detail", kwargs={"slug": self.slug})

    def get_full_address(self):
        if self.address and self.district:
            return "%s, %s" % (self.address, self.district)
        elif self.address:
            return self.address
        return self.district

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.supplier_name)
        super(Supplier, self).save(*args, **kwargs)

    def __str__(self):
        return self.supplier_name
