from rest_framework import serializers
from .models import Bank

class BankSerializer(serializers.ModelSerializer):
# to acess model data
    class meta:
        model = Bank
        field ={'ifsc ',' bank_id','branch','address','city','district','state'}

