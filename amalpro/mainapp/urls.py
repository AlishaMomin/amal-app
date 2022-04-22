from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customers, name='customers'),
    path('api/customer', views.postCustomer, name = "post_customer")
]