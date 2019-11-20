from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from rest_framework.decorators import api_view
from .models import Bank
from .serializers import BankSerializer
import xlrd

# Create your views here
loc =("./userbankdetails/details.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
#for row 0 and column 0
# sheet.cell_value(0,0)
# sheet.cell_value(0,0)
def some_name(request):
    for i in range(sheet.nrows):
        ifsc = (sheet.cell_value(i,0))
        bank_id = (sheet.cell_value(i, 1))
        branch = (sheet.cell_value(i, 2))
        address = (sheet.cell_value(i, 3))
        city = (sheet.cell_value(i, 4))
        district = (sheet.cell_value(i, 5))
        state = (sheet.cell_value(i, 6))
        bank_name = (sheet.cell_value(i,7))
        instance = Bank.objects.create(ifsc=ifsc,bank_id=bank_id,branch=branch,address=address,
                                       city=city,district=district,state=state ,bank_name=bank_name)
        print('instance')
    return  "completed"
@api_view(['GET'])
def bank_details(request):
    ifs = request.query_params['ifsc']
    print(ifs)
    Bank_details = Bank.objects.filter(ifsc=ifs)
    application = serialize('json',Bank_details)
    print(Bank_details)
    print(application)
    return HttpResponse(application)

@api_view(['GET'])
def bankname(request):
 bname=request.query_params['bank_name']
 bcity= request.query_params['city']
 print(bcity)
 print(bname)
 user= Bank.objects.filter(bank_name=bname,city=bcity).only("branch")
 application = BankSerializer(user,many=True)
 print(user)
 print(application)
 return HttpResponse(application)


