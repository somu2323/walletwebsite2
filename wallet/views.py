# wallet/views.py

from django.shortcuts import render
from .models import Transaction

def dashboard(request):
    transactions = Transaction.objects.all()
    total_sent = transactions.filter(transaction_type="sent").count()
    total_received = transactions.filter(transaction_type="received").count()
    
    # Prepare data for the charts
    # Example: monthly transaction counts
    monthly_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
    monthly_data = [500, 700, 800, 600, 900, 1000, 750]  # Replace with actual data

    context = {
        'transactions': transactions,
        'total_sent': total_sent,
        'total_received': total_received,
        'monthly_labels': monthly_labels,
        'monthly_data': monthly_data,
    }
    return render(request, 'wallet/dashboard.html', context)

# Example data for transactions (replace with database queries)
transactions_data = [
    {'date': '2024-11-01', 'time': '10:15 AM', 'type': 'Credit', 'transaction_id': 'TXN001', 'value': 500},
    {'date': '2024-11-02', 'time': '02:30 PM', 'type': 'Debit', 'transaction_id': 'TXN002', 'value': 300},
    {'date': '2024-11-03', 'time': '09:45 AM', 'type': 'Credit', 'transaction_id': 'TXN003', 'value': 200},
]

def transactions_view(request):
    return render(request, 'wallet/transactions.html', {'transactions': transactions_data})

def settings(request):
    return render(request, 'wallet/settings.html')

def support(request):
    return render(request, 'wallet/support.html')

def send_money(request):
    return render(request, 'wallet/send_money.html')

def receive_money(request):
    return render(request, 'wallet/receive_money.html')


