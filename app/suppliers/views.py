from django.db.models import Q
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import SupplierCreateForm, SupplierUpdateForm
from .models import Supplier


class SupplierSearchView(ListView):
    model = Supplier
    paginate_by = 10
    queryset = Supplier.objects.all()

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Supplier.objects.filter(
                Q(supplier_name__icontains=query)
                | Q(tags__icontains=query)
                | Q(email__icontains=query)
                | Q(phone__icontains=query)
                | Q(description__icontains=query)
                | Q(address__icontains=query)
                | Q(district__icontains=query)
            )
        else:
            return Supplier.objects.all()


class SupplierListView(ListView):
    model = Supplier
    paginate_by = 10
    ordering = ["supplier_name"]


class SupplierDetailView(DetailView):
    model = Supplier


class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierCreateForm


class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierCreateForm
    template_name_suffix = "_update_form"
