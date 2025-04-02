from django.urls import path
from .views import WalletCreateView, WalletListView

urlpatterns = [
    path("", WalletListView.as_view(), name="wallet-list"),
    path("create/", WalletCreateView.as_view(), name="wallet-create"),
]
