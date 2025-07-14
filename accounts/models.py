from django.db import models
from django.contrib.auth.models import User

class BankAccount(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Account (Balance: {self.balance}"