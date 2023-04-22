from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response

from apps.categories.models import Category
from apps.categories.serializers import (
    CategoryListSerializer,
    CategoryDetailSerializer
)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()

    
class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]