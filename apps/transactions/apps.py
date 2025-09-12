from django.apps import AppConfig

class TransactionsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.transactions'

    def ready(self):
        import apps.transactions.signals  # 👈 เพิ่มบรรทัดนี้เพื่อโหลด signals
