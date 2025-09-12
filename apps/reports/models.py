from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class DayReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    total_income = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_expenses = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_gain = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_transaction = models.PositiveIntegerField(default=0)
    total_category = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('date', 'user')
        verbose_name = "Daily Report"
        verbose_name_plural = "Daily Reports"
        ordering = ['-date']

    def __str__(self):
        return f"รายงานประจำวันที่ {self.date} - {self.user.username}"


class MonthlyReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    total_income = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_expenses = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_gain = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_transaction = models.PositiveIntegerField(default=0)
    total_category = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Monthly Report"
        verbose_name_plural = "Monthly Reports"
        ordering = ['-start_date']

    def __str__(self):
        return f"รายงานประจำเดือนที่ {self.user.username} ({self.start_date} to {self.end_date})"
    
    
class YearReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    total_income = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_expenses = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_gain = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_transaction = models.PositiveIntegerField(default=0)
    total_category = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('start_date', 'end_date', 'user')
        verbose_name = "Yearly Report"
        verbose_name_plural = "Yearly Reports"
        ordering = ['-start_date']

    def __str__(self):
        return f"รายงานประจำปี {self.start_date.year} - {self.user.username}"

