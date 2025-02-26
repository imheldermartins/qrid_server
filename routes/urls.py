from django.urls import include, path

urlpatterns = [
    path("transactions/", include("transactions.urls")),  # /api/services/
    # path("products/", include("products.urls")),  # /api/products/
    # path("clients/", include("clients.urls")),  # /api/clients/
]
