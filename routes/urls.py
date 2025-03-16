from django.urls import include, path

urlpatterns = [
    path("user/", include("apps.accounts.urls")),
    path("transactions/", include("apps.transactions.urls")),  # /api/transactions/
    path("categories/", include("apps.categories.urls")),  # /api/categories/
    path("wallets/", include("apps.wallets.urls")),  # /api/wallets/
]
