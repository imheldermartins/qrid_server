from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import WalletSerializer
from .models import Wallet


class WalletCreateView(generics.CreateAPIView):
    """(POST)
    Create a new wallet for the authenticated user.
    """

    permission_classes = (IsAuthenticated,)
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WalletListView(generics.ListAPIView):
    """(GET)
    List all wallets of the authenticated user.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = WalletSerializer

    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user)
