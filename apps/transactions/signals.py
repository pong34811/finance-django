from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction
from calendar import monthrange
from datetime import date as date_class

from apps.reports.views import (
    generate_day_report,
    generate_monthly_report,
    generate_year_report,  # อย่าลืมเพิ่มใน views.py ถ้ายังไม่มี
)


@receiver(post_save, sender=Transaction)
def auto_generate_reports(sender, instance, created, **kwargs):
    if not created:
        return

    user = instance.user
    tx_date = instance.date.date()  # แปลง datetime เป็น date object

    # ----------- สร้าง DayReport ผ่านฟังก์ชัน ----------- 
    generate_day_report(user=user, date=tx_date)

    # ----------- สร้าง MonthlyReport ผ่านฟังก์ชัน ----------- 
    start_month = tx_date.replace(day=1)
    end_month = tx_date.replace(day=monthrange(tx_date.year, tx_date.month)[1])
    generate_monthly_report(user=user, start_date=start_month, end_date=end_month)

    # ----------- สร้าง YearReport ผ่านฟังก์ชัน (ถ้ามี) ----------- 
    start_year = date_class(tx_date.year, 1, 1)
    end_year = date_class(tx_date.year, 12, 31)
    generate_year_report(user=user, start_date=start_year, end_date=end_year)
