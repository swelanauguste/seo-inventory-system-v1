from django import forms
from django.forms import widgets

from .models import Bill


class BillCreateForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = "__all__"
        exclude = ["created_by", "updated_by", "slug"]
        

class BillUpdateForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = "__all__"
        exclude = ["created_by", "updated_by", "slug"]

