from django import forms

class DepositForm(forms.Form):
    amount = forms.DecimalField(
        max_digits = 12,
        decimal_places = 2,
        min_value = 0.01,
        label = "Deposit Amount:"
    )
    
    