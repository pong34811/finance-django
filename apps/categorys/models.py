import uuid
from django.db import models
from framework.models import BaseModel


class Category(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    @property
    def total_transaction(self):
        return self.transaction_set.count()
