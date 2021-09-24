from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from mixins.assets import DISTRICT_LIST, TimeStampMixin


class Category(TimeStampMixin):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["slug"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("suppliers:category_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Supplier(TimeStampMixin):
    supplier_name = models.CharField("supplier's name", max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category, blank=True)
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


class SupplierAccountNumber(TimeStampMixin):
    supplier = models.ForeignKey(
        Supplier, related_name="supplier_account_numbers", on_delete=models.CASCADE
    )
    account_number = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.account_number
