from django.urls import path

from apps.products.views import (
    ProductDetailUpdateView,
    ProductListView,
    ProductCreateView
)


urlpatterns = [
    path('<int:pk>', ProductDetailUpdateView.as_view()),
    path('list/', ProductListView.as_view()),
    path('create/', ProductCreateView.as_view()),
]
