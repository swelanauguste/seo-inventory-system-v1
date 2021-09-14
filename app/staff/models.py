from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

User = settings.AUTH_USER_MODEL


from mixins.assets import TimeStampMixin


class Position(TimeStampMixin):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Department(TimeStampMixin):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    staff = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    employment_id = models.CharField(max_length=10, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    ext = models.CharField(max_length=25, null=True, blank=True)
    position = models.ForeignKey(
        Position, on_delete=models.SET_NULL, null=True, blank=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True
    )
    is_seo = models.BooleanField("SEO", default=False)
    is_ag = models.BooleanField("AG", default=False)

    def get_absolute_url(self):
        return reverse("staff:detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("staff:update", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Staff"
        verbose_name_plural = "Staff"

    def get_staff_initials(self):
        if self.first_name and self.last_name:
            return ("%s%s" % (self.first_name[0], self.last_name[0])).upper()
        return (self.staff.username[0]).upper()

    def get_full_name(self):
        if self.first_name and self.last_name:
            return "%s, %s" % (self.last_name, self.first_name)
        return self.staff.username

    def get_user_email(self):
        return self.staff.email

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.staff)
        super(Staff, self).save(*args, **kwargs)

    def __str__(self):
        if self.first_name and self.last_name:
            return "%s, %s" % (self.last_name, self.first_name)
        return self.staff.username
