from django.urls import path

from apps.categories.views import (
    CategoryDetailView,
    CategoryListView, 
    CategoryUpdateView, 
    CategoryCreateView
)


urlpatterns = [
    path('list/', CategoryListView.as_view()),
    path('create/', CategoryCreateView.as_view()),
    path('<int:pk>', CategoryDetailView.as_view()),
    path('update/<int:pk>', CategoryUpdateView.as_view()),
]
