from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),

    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name= "logout"),
    path("login", views.login_request, name="login"),
    path("password_reset", views.password_reset_request, name="password_reset"),

    path("customer_dashboard", views.customerdashboard, name="customerdashboard"),

    path('customers/', views.customers, name='customers'),
    path('api/customer', views.postCustomer, name = "post_customer"),

    path('listing/', views.listing, name='listing'),
    path('api/listing', views.postListing, name = "post_listing"),

    path('booking/', views.booking, name='booking'),
    path('api/booking', views.postBooking, name = "post_booking"),
    
    path('serviceprovider/', views.serviceprovider, name='serviceprovider'),
    path('viewSP/', views.viewserviceprovider, name='viewserviceprovider'),

    path('api/sp', views.postServiceprovider, name = "post_sp"),
    
    path('test/', views.test, name = "test"),
    path('prompt/', views.prompt, name = "prompt"),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),      

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

