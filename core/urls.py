from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.view_all_customers, name='customers'),
    path('customers/<id>/', views.customer_details, name='customer_details'),
    # path('customers/<id>/transfer/', views.transfer, name='transfer'),
    path('transfer/', views.transfer, name='transfer'),
    path('transfer/<id>/', views.transfer_details, name='transfer_d'),
]
