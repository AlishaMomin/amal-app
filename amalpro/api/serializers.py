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

