from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path("register", views.register_request, name="register"),
    
    path("login", views.login_request, name="login"),

    path('customers/', views.customers, name='customers'),
    path('api/customer', views.postCustomer, name = "post_customer"),

    path('listing/', views.listing, name='listing'),
    path('api/listing', views.postListing, name = "post_listing"),

    path('booking/', views.booking, name='booking'),
    path('api/booking', views.postBooking, name = "post_booking"),
    
    path('serviceprovider/', views.serviceprovider, name='serviceprovider'),
    path('api/sp', views.postServiceprovider, name = "post_sp"),
    
    path('test/', views.test, name = "test")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

