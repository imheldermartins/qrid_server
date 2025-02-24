from django.urls import path

from . import views

urlpatterns = [path("get_all_services", views.get_services, name="get_all_services")]
