from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_transaction', 'created_at', 'updated_at', 'created_by', 'updated_by')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', 'total_transaction')
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Category ,CategoryAdmin)