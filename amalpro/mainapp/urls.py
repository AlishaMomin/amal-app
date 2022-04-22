from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customers, name='customers'),
<<<<<<< HEAD
    path('api/customer', views.postCustomer, name = "post_customer"),
    path('test/', views.test, name="test"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
    path('listing/', views.listing, name='listing'),
    path('booking/', views.booking, name='booking'),
    path('serviceprovider/', views.serviceprovider, name='serviceprovider'),
    path('api/customer', views.postCustomer, name = "post_customer"),
    path('api/sp', views.postServiceprovider, name = "post_sp")
]
>>>>>>> 663d1f74ab16145e5442ca7fe860f19f805480e6
