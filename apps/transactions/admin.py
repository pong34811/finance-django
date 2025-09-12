from django.contrib import admin
from apps.transactions.models import Transaction
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'category', 'date', 'created_at', 'updated_at', 'created_by', 'updated_by')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
    search_fields = ('name',)
    list_filter = ('type', 'category')
    ordering = ('-date',)


admin.site.register(Transaction ,TransactionAdmin)