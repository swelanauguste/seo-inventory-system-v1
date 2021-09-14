from django import forms

from .models import Staff


class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"
        exclude = [
            "staff",
            "slug",
            "employment_id",
            "position",
            "department",
            "is_seo",
            "is_ag",
        ]
