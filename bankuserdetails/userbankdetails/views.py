import csv
import io

from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

from .models import Bank


# Create your views here
#this code belongs that super user add the file
@permission_required('admin.can_add_log_entry')
def userdata_upload(request):
    template = "userdetails.html"
    prompt = {
        'order':'order of the csv should be ifsc, bank_id, branch , address,city,district,state'
    }
    if request.method == 'GET':
        return render(request,template,prompt)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string,delimeter=',',quotechar="|"):
        _, created = Bank.objects.update_or_create(
            ifsc =column[0],
            bank_id = column[1],
            branch = column[2],
            address = column[3],
            city = column[4],
            district = column[5],
            state = column[6]
        )
    context = {}
    return render(request,template,context)



