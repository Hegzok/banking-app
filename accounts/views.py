from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import DepositForm
from .models import  BankAccount
from django.db import transaction
from django.http import HttpResponse
from accounts.models import BankAccount
from django.contrib.auth import login
from .forms import RegistrationForm


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

@login_required
def deposit_view(request):
    
    if request.method == "POST":
        form = DepositForm(request.POST)
        
        if form.is_valid():
            amount = form.cleaned_data["amount"]
            
            with transaction.atomic():
                account = BankAccount.objects.select_for_update().get(user=request.user)
                account.balance += amount
                account.save()
                
                return redirect("account_detail")
    else:
        form = DepositForm();
        
    context = {
        "form": form,
    }
        
    return render(request, "accounts/deposit.html", context)

@transaction.atomic
def registration_view(request):
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        
        if (form.is_valid()):
            new_user = form.save()
            BankAccount.objects.create(user=new_user, balance=0)
            login(request, new_user)
            return redirect("account_detail")
    else:
       form = RegistrationForm()
            
    context = {
        "form": form
    }
    
    return render(request, "accounts/register.html", context)
        
        