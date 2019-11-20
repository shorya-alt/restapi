from django.urls import path
from . import views

urlpatterns = [
path('upload/',views.some_name,name='advisor'),
path('bank_details/',views.bank_details,name='bank_details'),
path('bankname/',views.bankname,name='bankname')
]
