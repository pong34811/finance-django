# categorys_app/urls.py

from django.urls import path
from .views import (
    CategoryListAPIView,
    CategoryRetrieveAPIView,
    CategoryCreateAPIView,
    CategoryUpdateAPIView,
    CategoryDestroyAPIView,
)

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name='category-list'),
    path('<uuid:id>/', CategoryRetrieveAPIView.as_view(), name='category-detail'),
    path('create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('<uuid:id>/update/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('<uuid:id>/delete/', CategoryDestroyAPIView.as_view(), name='category-delete'),
]
