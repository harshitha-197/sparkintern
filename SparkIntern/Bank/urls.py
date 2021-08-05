from django.urls import path, include
from . import views
urlpatterns =[
    path('',views.home,name='home'),
    path('home1',views.home1,name='home1'),
    path('cust-details',views.cust_data,name='cust_data'),
    path('transactons',views.transactions,name='transactions'),
    path('transfer-page',views.sendmoney,name='send-money'),
    path('customer-data',views.customer_details,name='customerdetails'),
    path('insert',views.insertdata,name='insert')
]