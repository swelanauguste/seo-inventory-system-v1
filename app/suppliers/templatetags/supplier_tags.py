import json
from django import template
from django.utils.safestring import mark_safe

from ..models import Category

register = template.Library()


@register.simple_tag
def supplier_categories_tags():
    return Category.objects.all().order_by("slug")


# @register.simple_tag
# def pro_2013_64():
#     return Installation.objects.filter(product__name='PROFESSIONAL 2013 64-BIT').count()


# @register.simple_tag
# def pro_2013_32():
#     return Installation.objects.filter(product__name='STANDARD 2013 32-BIT').count()


# @register.simple_tag
# def total_products():
#     return Product.objects.count()


# @register.simple_tag
# def total_customers():
#     return Customer.objects.count()
