from django.urls import path

from . import views

app_name = "purchases"


urlpatterns = [
    path("", views.BillListView.as_view(), name="list"),
    path("new/", views.BillCreateView.as_view(), name="create"),
    path("detail/<slug:slug>", views.BillDetailView.as_view(), name="detail"),
    path("update/<slug:slug>", views.BillUpdateView.as_view(), name="update"),
]
