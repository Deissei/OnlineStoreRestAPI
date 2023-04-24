from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.validators import ValidationError

from apps.products.serializers import (
    ImageProductSerializer,
    ProductListSerializer,
    ProductSerializer 
)

from apps.products.models import Product
from apps.products.permissions import IsManufacturer, IsUserWho


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductDetailUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsManufacturer]


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsUserWho]

    def perform_create(self, serializer):
        serializer.save(manufacturer=self.request.user)
        return serializer
    
    def get_permissions(self):
        if self.request.user.user_who == "ПОКУПАТЕЛЬ":
            raise ValidationError("Ты не продавец")
        else:
            return [IsAuthenticated()]