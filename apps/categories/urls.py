from django.urls import path

from .views import CategoryCreateView, CategoryListView

urlpatterns = [
    path("", CategoryListView.as_view(), name="categories_list"),
    path("create/", CategoryCreateView.as_view(), name="categories_create"),
]
