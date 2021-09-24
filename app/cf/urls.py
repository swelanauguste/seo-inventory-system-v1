from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mixins.views import Index

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("suppliers/", include("suppliers.urls", namespace="suppliers")),
    path("purchases/", include("purchases.urls", namespace="purchases")),
    path("staff/", include("staff.urls", namespace="staff")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
