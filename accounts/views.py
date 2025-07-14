from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import BankAccount


# Create your views here.
@login_required
def account_detail_view(request):
    
    try:
        account = BankAccount.objects.get(user=request.user)
    except BankAccount.DoesNotExist:
        return HttpResponse("You don't have an account yet")
    
    context = {
        "account": account
    }
    
    return render(request, "accounts/account_detail.html", context)