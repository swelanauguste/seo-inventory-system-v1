from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView

from .forms import StaffUpdateForm
from .models import Staff


class SearchSearchView(ListView):
    model = Staff
    paginate_by = 10
    queryset = Staff.objects.all()

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Staff.objects.filter(
                Q(supplier_name__icontains=query)
                | Q(tags__icontains=query)
                | Q(email__icontains=query)
                | Q(phone__icontains=query)
                | Q(description__icontains=query)
                | Q(address__icontains=query)
                | Q(district__icontains=query)
            )
        else:
            return Staff.objects.all()


class StaffListView(ListView):
    model = Staff


class StaffDetailView(DetailView):
    model = Staff


class StaffUpdateView(UpdateView):
    model = Staff
    form_class = StaffUpdateForm
    template_name_suffix = "_update_form"
