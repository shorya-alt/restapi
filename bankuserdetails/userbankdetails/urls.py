from django.urls import path
from . import views

urlpatterns = [
path('upload/',views.some_name,name='advisor')
]
