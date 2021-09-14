from django.urls import path

from . import views


app_name = "staff"


urlpatterns = [
    path("", views.StaffListView.as_view(), name="list"),
    path("detail/<slug:slug>", views.StaffDetailView.as_view(), name="detail"),
    path("update/<slug:slug>", views.StaffUpdateView.as_view(), name="update"),
]
