from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Supplier
from .forms import SupplierCreateForm, SupplierUpdateForm


class SupplierListView(ListView):
    model = Supplier


class SupplierDetailView(DetailView):
    model = Supplier


class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierCreateForm


class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierCreateForm
    template_name_suffix = '_update_form'