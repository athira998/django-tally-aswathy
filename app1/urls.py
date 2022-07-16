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
    path('load_unit_compound',views.load_unit_compound,name='load_unit_compound'),
    
    path('load_stock_item_creation',views.load_stock_item_creation,name='load_stock_item_creation'),
    path('load_company_price',views.load_company_price,name='load_company_price'),
    path('load_pan_cin',views.load_pan_cin,name='load_pan_cin'),
    path('godown_creation',views.godown_creation,name='godown_creation'),
    path('load_tds',views.load_tds,name='load_tds'),
    path('load_person_res',views.load_person_res,name='load_person_res'),
    path('load_gst_details',views.load_gst_details,name='load_gst_details'),
    path('load_gst',views.load_gst,name='load_gst'),
    path('load_lut_bond',views.load_lut_bond,name='load_lut_bond'),
    path('load_gst_details_c',views.load_gst_details_c,name='load_gst_details_c'),
    path('load_rev',views.load_rev,name='load_rev'),







    
]