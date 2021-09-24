from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import BillCreateForm, BillUpdateForm
from .models import Bill


class BillListView(LoginRequiredMixin, ListView):
    model = Bill
    paginate_by = 10


class BillDetailView(LoginRequiredMixin, DetailView):
    model = Bill


class BillCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Bill
    form_class = BillCreateForm
    success_message = "%(purchase_order_number)s was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class BillUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Bill
    form_class = BillUpdateForm
    template_name_suffix = "_update_form"
    success_message = "%(purchase_order_number)s was updated successfully"

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
