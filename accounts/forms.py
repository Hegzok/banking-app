from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DepositForm(forms.Form):
    amount = forms.DecimalField(
        max_digits = 12,
        decimal_places = 2,
        min_value = 0.01,
        label = "Deposit Amount:"
    )
    
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta(UserCreationForm):
        model = User
        fields = ("username", "email")