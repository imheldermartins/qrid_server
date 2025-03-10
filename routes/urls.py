from django.urls import include, path

urlpatterns = [
    path("", include("accounts.urls")),
    path("transactions/", include("transactions.urls")),  # /api/transactions/
]
