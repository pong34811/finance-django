from django.contrib import admin
from .models import MonthlyReport, DayReport, YearReport
from .export_mouth import export_as_excel


export_as_excel.short_description = "Export selected reports as Excel"

class MonthlyReportAdmin(admin.ModelAdmin):
    actions = [export_as_excel]
    list_display = (
        'start_date', 
        'end_date',
        'total_income', 
        'total_expenses', 
        'total_gain', 
        'total_transaction', 
        'total_category',
        'created_at',
        'user', 
    )
    list_filter = ('user', 'start_date', 'end_date')
    search_fields = ('user__username',)
    ordering = ('-start_date',)
    date_hierarchy = 'start_date'
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('user', 'start_date', 'end_date')
        }),
        ('Summary', {
            'fields': (
                'total_income',
                'total_expenses',
                'total_gain',
                'total_transaction',
                'total_category',
            )
        }),
        ('Metadata', {
            'fields': ('created_at',),
        }),
    )

class DayReportAdmin(admin.ModelAdmin):
    actions = [export_as_excel]
    list_display = (
        'date',
        'total_income',
        'total_expenses',
        'total_gain',
        'total_transaction',
        'total_category',
        'created_at',
        'user',
    )
    list_filter = ('user', 'date')
    search_fields = ('user__username',)
    ordering = ('-date',)
    date_hierarchy = 'date'
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('user', 'date')
        }),
        ('Summary', {
            'fields': (
                'total_income',
                'total_expenses',
                'total_gain',
                'total_transaction',
                'total_category',
            )
        }),
        ('Metadata', {
            'fields': ('created_at',),
        }),
    )

class YearReportAdmin(admin.ModelAdmin):
    actions = [export_as_excel]
    list_display = (
        'start_date',
        'end_date',
        'total_income',
        'total_expenses',
        'total_gain',
        'total_transaction',
        'total_category',
        'created_at',
        'user',
    )
    list_filter = ('user', 'start_date', 'end_date')
    search_fields = ('user__username',)
    ordering = ('-start_date',)
    date_hierarchy = 'start_date'
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('user', 'start_date', 'end_date')
        }),
        ('Summary', {
            'fields': (
                'total_income',
                'total_expenses',
                'total_gain',
                'total_transaction',
                'total_category',
            )
        }),
        ('Metadata', {
            'fields': ('created_at',),
        }),
    )

admin.site.register(MonthlyReport, MonthlyReportAdmin)
admin.site.register(DayReport, DayReportAdmin)
admin.site.register(YearReport, YearReportAdmin)



