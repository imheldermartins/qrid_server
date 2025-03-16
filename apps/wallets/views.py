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
