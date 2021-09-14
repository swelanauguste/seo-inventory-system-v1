from django import forms
from django.forms import widgets

from .models import Supplier


class SupplierCreateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        exclude = ["created_by", 'updated_by', 'slug', 'is_deleted']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 20}),
            'tags': forms.Textarea(attrs={'rows': 3, 'cols': 20}),
        }


class SupplierUpdateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        exclude = ["created_by", 'updated_by', 'slug', 'is_deleted']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 20}),
            'tags': forms.Textarea(attrs={'rows': 3, 'cols': 20}),
        }