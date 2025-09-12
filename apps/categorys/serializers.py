from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    total_transaction = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'total_transaction']
