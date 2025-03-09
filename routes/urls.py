from django.urls import include, path

urlpatterns = [
    path("", include("accounts.urls")),
    path("transactions/", include("transactions.urls")),  # /api/transactions/
    # path("products/", include("products.urls")),  # /api/products/
    # path("clients/", include("clients.urls")),  # /api/clients/
]
