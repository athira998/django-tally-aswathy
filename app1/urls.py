from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),



    path('load_stock_group',views.load_stock_group,name='load_stock_group'),
    path('load_stock_catagory',views.load_stock_catagory,name='load_stock_catagory'),
    path('load_unit_creation',views.load_unit_creation,name='load_unit_creation'),
    path('load_stock_item',views.load_stock_item,name='load_stock_item'),
    path('load_company_price',views.load_company_price,name='load_company_price'),
    path('load_pan_cin',views.load_pan_cin,name='load_pan_cin'),




    
]