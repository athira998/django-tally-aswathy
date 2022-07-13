from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home.html')

def group(request):
    return render(request, 'groups.html')

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def costcentr(request):
    return render(request, 'costcentr.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')


def load_stock_group(request):
    return render(request,'stock_group.html')


def load_stock_catagory(request):
    return render(request,'stock_catagory.html')

def load_unit_creation(request):
    return render(request,'unit_creation.html')

def load_stock_item(request):
    return render(request,'stock_item.html')

def load_company_price(request):
    return render(request,'company_price.html')


def load_pan_cin(request):
    return render(request,'pan_cin.html')
