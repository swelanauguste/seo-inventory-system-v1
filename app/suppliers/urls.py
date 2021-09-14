from django.urls import path

from . import views

app_name = "suppliers"

urlpatterns = [
    path("", views.SupplierListView.as_view(), name="list"),
    path("detail/<slug:slug>", views.SupplierDetailView.as_view(), name="detail"),
    path("update/<slug:slug>", views.SupplierUpdateView.as_view(), name="update"),
    path("create/", views.SupplierCreateView.as_view(), name="create"),
]
