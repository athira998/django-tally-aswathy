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

def load_unit_compound(request):
    return render(request,'unit_compound.html')


def load_stock_item_creation(request):
    return render(request,'stock_item_creation.html')

def load_company_price(request):
    return render(request,'company_price.html')


def load_pan_cin(request):
    return render(request,'pan_cin.html')

def godown_creation(request):
    return render(request,'godown.html')

def load_tds(request):
    return render(request,'tds_details.html')

def load_person_res(request):
    return render(request,'person_res.html')

def load_gst_details(request):
    return render(request,'gst_details.html')

def load_gst(request):
    return render(request,'gst.html')

def load_lut_bond(request):
    return render(request,'lut_bond.html')

def load_gst_details_c(request):
    return render(request,'gst_details_c.html')

def load_rev(request):
    return render(request,'revised.html')
