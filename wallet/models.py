from django.db import models

class Transaction(models.Model):
    TYPES = [
        ('sent', 'Sent'),
        ('received', 'Received'),
    ]
    date = models.DateField()
    time = models.TimeField()
    transaction_type = models.CharField(max_length=10, choices=TYPES)
    transaction_id = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.transaction_type} - ${self.value}"
