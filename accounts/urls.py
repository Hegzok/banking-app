from django.urls import path
from . import views

urlpatterns = [
    path("my-account/", views.account_detail_view, name="account_detail"),
    path("deposit/", views.deposit_view, name="deposit"),
]