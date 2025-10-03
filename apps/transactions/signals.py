import os
import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Transaction
from calendar import monthrange
from datetime import date as date_class
import requests
from .discord_form.message_template import MESSAGE_CREATED_TEMPLATE
from django.db import transaction as db_transaction

logger = logging.getLogger(__name__)


from apps.reports.views import (
    generate_day_report,
    generate_monthly_report,
    generate_year_report,  # อย่าลืมเพิ่มใน views.py ถ้ายังไม่มี
)

# auto-generate reports when a Transaction is created
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

# ส่งข้อความไปยัง Discord
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1417451493908549784/d46gfxbQLGK68eVclCRb7Jh91VXTH5AB8BY5T0qB5Jbvjj_0Qoj46v1mmRybF2pS3r26"

def send_discord_message(content: str, files=None, timeout: int = 10):
    data = {"content": content}
    files_payload = {
        f"file{idx}": (os.path.basename(f.name), f.open("rb").read())
        for idx, f in enumerate(files or [])
    }
    requests.post(DISCORD_WEBHOOK_URL, data=data, files=files_payload or None, timeout=timeout)

@receiver(post_save, sender=Transaction)
def transaction_saved(sender, instance, created, **kwargs):
    title = "Transaction Created" if created else "Transaction Updated"
    message_text = MESSAGE_CREATED_TEMPLATE.format(
        title=title,
        date=instance.date.strftime("%Y-%m-%d %H:%M:%S"),
        name=instance.name,
        price=instance.price,
        type=instance.get_type_display()
    )

    def _send_after_commit():
        # re-fetch instance to ensure fresh relations (และ prefetch files)
        try:
            tx = sender.objects.prefetch_related("files").get(pk=instance.pk)
        except sender.DoesNotExist:
            return

        # สร้าง list ของ FieldFile objects (tf.file) เพื่อส่งให้ send_discord_message
        file_fields = [tf.file for tf in tx.files.all()]
        send_discord_message(message_text, files=file_fields)

    # เรียก callback หลังจาก DB transaction ถูก commit แล้ว
    db_transaction.on_commit(_send_after_commit)

        
@receiver(post_delete, sender=Transaction)
def transaction_deleted(sender, instance, **kwargs):
    message = f"Transaction Deleted: {instance.name} - {instance.price} ({instance.get_type_display()})"
    send_discord_message(message)