from django.urls import path
from .views import (
    TransactionListAPIView,
    TransactionRetrieveAPIView,
    TransactionCreateAPIView,
    TransactionUpdateAPIView,
    TransactionDestroyAPIView,
)

urlpatterns = [
    path('', TransactionListAPIView.as_view(), name='transaction-list'),
    path('<uuid:id>/', TransactionRetrieveAPIView.as_view(), name='transaction-detail'),
    path('create/', TransactionCreateAPIView.as_view(), name='transaction-create'),
    path('<uuid:id>/update/', TransactionUpdateAPIView.as_view(), name='transaction-update'),
    path('<uuid:id>/delete/', TransactionDestroyAPIView.as_view(), name='transaction-delete'),
]
