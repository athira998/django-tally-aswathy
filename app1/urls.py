from django.urls import path,include
from.import views


urlpatterns = [
    
    path('',views.index,name='index'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),

    
]