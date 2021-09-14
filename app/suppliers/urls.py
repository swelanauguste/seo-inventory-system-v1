from django.urls import path

from . import views

app_name = "suppliers"

urlpatterns = [
    path("", views.SupplierListView.as_view(), name="list"),
    path("search", views.SupplierSearchView.as_view(), name="search"),
    path("detail/<slug:slug>", views.SupplierDetailView.as_view(), name="detail"),
    path("update/<slug:slug>", views.SupplierUpdateView.as_view(), name="update"),
    path("add/", views.SupplierCreateView.as_view(), name="create"),
]
