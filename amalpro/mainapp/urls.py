from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customers, name='customers'),
    path('api/customer', views.postCustomer, name = "post_customer"),
    path('test/', views.test, name="test"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)