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

def settings_view(request):
    return render(request, 'wallet/settings.html')  # This renders the settings page
