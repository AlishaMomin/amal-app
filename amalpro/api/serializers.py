from rest_framework import serializers
from .models import Customer, ServiceProviders, Booking, Listing

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'fullNameCustomer',
            'cnicCustomer',
            'addressCustomer',
            'cityCustomer',
            'dobCustomer',
            'ReviewCustomer'
        )

class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProviders
        fields = (
            'fullNameSP',
            'cnicSP',
            'addressSP',
            'citySP',
            'dobSP',
            'languageSP'
        )

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'bookingDate',
            'bookingSlot',
            'serviceType',
            'ServiceProviderID'
        )

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = (
            'Charges',
            'serviceType',
        )    