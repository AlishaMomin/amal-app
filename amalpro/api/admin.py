from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Booking)
admin.site.register(Customer)
admin.site.register(ServiceProviders)
admin.site.register(Listing)