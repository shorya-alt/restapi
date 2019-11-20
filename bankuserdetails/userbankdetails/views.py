from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Bank
from .serializers import BankSerializer
import xlrd

# Create your views here
loc =("/home/hp/PycharmProject/corepython/banksdetails/bankuserdetails/details.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
#for row 0 and column 0
# sheet.cell_value(0,0)
def some_name(request):
    for i in range(sheet.nrows):
        ifsc = (sheet.cell_value(i,0))
        bank_id = (sheet.cell_value(i,1))
        branch = (sheet.cell_value(i, 2))
        address = (sheet.cell_value(i, 3))
        city = (sheet.cell_value(i, 4))
        district = (sheet.cell_value(i, 5))
        state = (sheet.cell_value(i, 6))
        bank_name = (sheet.cell_value(i,7))
        instance = Bank.objects.create(ifsc=ifsc,bank_id=bank_id,branch=branch,address=address,city=city,district=district,state=state
                                      , bank_name=bank_name)
        print('instance')
    return  "completed"