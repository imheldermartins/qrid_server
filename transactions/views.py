from rest_framework import generics

# from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionListView(generics.ListAPIView):
    """(GET)
    Get all objects on transactions schema
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailView(generics.RetrieveAPIView):
    """(GET)
    Get a only transaction based on <int:id> param
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
