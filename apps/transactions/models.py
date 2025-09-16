from django.db import models
import uuid
from apps.categorys.models import Category
from framework.models import BaseModel

class Transaction(BaseModel):
    class TransactionType(models.TextChoices):
        INCOME = 'income', 'รายรับ'
        EXPENSE = 'expense', 'รายจ่าย'
    

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=7, choices=TransactionType.choices)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    class Meta:
        ordering = ['-date']
        

    def __str__(self):
        return f"{self.name} ({self.get_type_display()}) - {self.price}"

class TransactionFile(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to="uploads/%Y-%m-%d")