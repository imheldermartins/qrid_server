from django.contrib import admin
from django.urls import path

# apps/
from services.views import service_list

urlpatterns = [path("admin/", admin.site.urls), path("", service_list)]
