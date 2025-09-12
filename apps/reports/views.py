from django.db.models import Sum, Count, Q
from apps.transactions.models import Transaction
from .models import MonthlyReport ,DayReport  ,YearReport

def generate_day_report(user, date):
    #quryset
    quryset = Transaction.objects.filter(
        user=user,
        date__date=date
    #logic to calculate totals
    ).aggregate(
        total_income=Sum('price', filter=Q(type=Transaction.TransactionType.INCOME)),
        total_expenses=Sum('price', filter=Q(type=Transaction.TransactionType.EXPENSE)),
        total_transaction=Count('id'),
        total_category=Count('category', distinct=True),
    )
    # Assign default values if None
    total_income = quryset['total_income'] or 0
    total_expenses = quryset['total_expenses'] or 0
    total_gain = total_income - total_expenses
    total_transaction = quryset['total_transaction']
    total_category = quryset['total_category']
    
    # สร้างหรืออัปเดตรายงาน
    report, _ = DayReport.objects.update_or_create(
        user=user,
        date=date,
        defaults={
            'total_income': total_income,
            'total_expenses': total_expenses,
            'total_transaction': total_transaction,
            'total_category': total_category,
            'total_gain': total_gain,
        }
    )
    return report

def generate_monthly_report(user, start_date, end_date):
    data = calculate_report(user, start_date, end_date)
    report, _ = MonthlyReport.objects.update_or_create(
        user=user,
        start_date=start_date,
        end_date=end_date,
        defaults=data
    )
    return report

def generate_year_report(user, start_date, end_date):
    data = calculate_report(user, start_date, end_date)
    report, _ = YearReport.objects.update_or_create(
        user=user,
        start_date=start_date,
        end_date=end_date,
        defaults=data
    )
    return report

def calculate_report(user, start_date, end_date):
    quryset = Transaction.objects.filter(
        user=user,
        date__date__gte=start_date,
        date__date__lte=end_date
    ).aggregate(
        total_income=Sum('price', filter=Q(type=Transaction.TransactionType.INCOME)),
        total_expenses=Sum('price', filter=Q(type=Transaction.TransactionType.EXPENSE)),
        total_transaction=Count('id'),
        total_category=Count('category', distinct=True),
    )

    total_income = quryset['total_income'] or 0
    total_expenses = quryset['total_expenses'] or 0
    total_gain = total_income - total_expenses
    total_transaction = quryset['total_transaction']
    total_category = quryset['total_category']
    
    return {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'total_gain': total_gain,
        'total_transaction': total_transaction,
        'total_category': total_category,
    }