from django.contrib import admin
from django.urls import include, path

# apps/
# from services.views import service_list

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", service_list)
    path("api/", include("services.urls"), name="services_urls"),
]
