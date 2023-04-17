from django.shortcuts import render
from django.contrib import messages
import random as rd
import string
from .models import Data
from django.core.paginator import Paginator
# Create your views here.


def gen_name(length):
    name = ''.join(rd.choices(string.ascii_uppercase, k=length))
    return name


def gen_contact(length):
    contact = ''.join([str(rd.randint(0, 9)) for _ in range(length)])
    return contact


def home(request):
    if request.method == "POST":
        number = int(request.POST['data-insert'])
        # print(number)
        insertcount = 0
        # name=namelist[rd.randint(0,len(namelist))]
        # contact="+91 "+str(rd.randint(1000000000,9999999999))
        # print(name,contact)
        if number > 0:
            try:
                for _ in range(number):
                    # name=rd.random(namelist)+rd.random(namelist)
                    name = gen_name(15)
                    contact = "+91 " + gen_contact(10)
                    # print(name,contact)
                    data = Data.objects.create(name=name, contact=contact)
                    data.save()
                    insertcount += 1
            except:
                messages.error(request, "Oops!! Some error occured."+str(insertcount) +
                               " data inserted.", extra_tags="alert alert-warning alert-dismissible fade show")
            messages.success(request, str(insertcount)+" data inserted successfully.",
                             extra_tags="alert alert-success alert-dismissible fade show")
        else:
            messages.error(request, "Please enter a valid value.",
                           extra_tags="alert alert-warning alert-dismissible fade show")
    return render(request, 'home.html')


def show(request):
    datas = Data.objects.all()
    paginator = Paginator(datas, 11)
    page = request.GET.get('page')
    datas = paginator.get_page(page)

    dict = request.GET.copy()
    params = dict.pop('page', True) and dict.urlencode()
    return render(request, 'showdata.html', {'datas': datas,'params':params})
