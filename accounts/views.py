from rest_framework import generics

# from rest_framework.response import Response
# from .models import Accounts

# from .serializers import TransactionSerializer


# class AccountSignUpView(generics.ListAPIView):
#     """(GET)
#     Get all objects on transactions schema
#     """

#     queryset = Accounts.objects.all()
#     # serializer_class = TransactionSerializer


# class AccountSignInView(generics.RetrieveAPIView):
#     """(GET)
#     Get a only transaction based on <int:id> param
#     """

#     queryset = Accounts.objects.all()
#     # serializer_class = TransactionSerializer
#     lookup_field = "id"
