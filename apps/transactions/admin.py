from django.contrib import admin
from apps.transactions.models import Transaction, TransactionFile

class TransactionFileInline(admin.TabularInline):
    model = TransactionFile
    extra = 1  # ช่องว่างเริ่มต้น
    max_num = 10  # สูงสุด 10 ไฟล์ต่อ Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'category', 'date', 'created_at', 'updated_at', 'created_by', 'updated_by')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
    search_fields = ('name',)
    list_filter = ('type', 'category')
    ordering = ('-date',)
    inlines = [TransactionFileInline]  # <-- ใส่ Inline ตรงนี้


class TransactionFileAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'file')
    search_fields = ('transaction__name',)
    list_filter = ('transaction__type',)

    
admin.site.register(Transaction ,TransactionAdmin)
admin.site.register(TransactionFile ,TransactionFileAdmin)