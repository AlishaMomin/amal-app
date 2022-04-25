from django.contrib import admin
from .models import *

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('bookingDate', 'bookingSlot', 'serviceType', 'SProvider')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fullNameCustomer', 'cnicCustomer', 'addressCustomer', 'cityCustomer', 'dobCustomer')

class ServiceProvidersAdmin(admin.ModelAdmin):
    list_display = ('fullNameSP', 'cnicSP', 'addressSP' , 'citySP', 'dobSP' , 'languageSP')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('Charges', 'serviceType')

admin.site.register(Booking, BookingAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(ServiceProviders, ServiceProvidersAdmin)
admin.site.register(Listing, ListingAdmin)