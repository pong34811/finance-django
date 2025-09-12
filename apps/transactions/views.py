from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer

# 🔹 List All Transactions
class TransactionListAPIView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# 🔹 Retrieve One Transaction
class TransactionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'id'


# 🔹 Create Transaction
class TransactionCreateAPIView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# 🔹 Update Transaction
class TransactionUpdateAPIView(generics.UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'id'


# 🔹 Delete Transaction
class TransactionDestroyAPIView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'id'
