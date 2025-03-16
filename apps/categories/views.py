from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import CategorySerializer

from .models import Category


class CategoryCreateView(generics.CreateAPIView):
    """(POST)
    Set a new category in the database.
    """

    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        # Define o usuário autenticado como o 'owner' automaticamente
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        # Retorna apenas as categorias do usuário autenticado
        return Category.objects.filter(owner=self.request.user)
