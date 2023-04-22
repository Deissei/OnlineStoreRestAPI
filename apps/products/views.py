from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from apps.products.serializers import (
    ImageProductSerializer,
    ProductListSerializer,
    ProductSerializer 
)

from apps.products.models import Product
from apps.products.permissions import IsManufacturer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductDetailUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_permissions(self):
        if self.request.method in ('PUT', 'DELETE', "UPDATE"):
            return IsManufacturer
        else:
            return IsAuthenticatedOrReadOnly



class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]