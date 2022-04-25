from django.db import models
from djongo import models


# Create your models here.

class Customer(models.Model):
    fullNameCustomer = models.CharField(max_length=255)
    cnicCustomer = models.CharField(max_length=13)
    addressCustomer = models.CharField(max_length=255)
    cityCustomer = models.CharField(max_length=25)
    dobCustomer = models.DateField()
    ReviewCustomer = models.TextField(max_length=10000)
    
    def __str__(self):
        return str(self.fullNameCustomer) + ", " + str(self.cityCustomer) 

class ServiceProviders(models.Model):
    ServiceProviderID = models.BigAutoField(primary_key=True)
    fullNameSP = models.CharField(max_length=255)
    cnicSP = models.CharField(max_length=13)
    addressSP = models.CharField(max_length=255)
    citySP = models.CharField(max_length=25)
    dobSP = models.DateField()
    MY_LANG_CHOICES = (
        ('ENG', 'English'),
        ('UR', 'Urdu'),
    )
    languageSP = models.CharField(max_length=3, choices=MY_LANG_CHOICES)
    
    def __str__(self):
        return str(self.fullNameSP) + ", " + str(self.citySP) 

class Booking(models.Model):
    bookingDate = models.DateField()
    BK_SLOT = (
        ('mor', 'Morning'),
        ('aft', 'Afternoon'),
        ('eve', 'Evening'),
    )
    bookingSlot = models.CharField(max_length=3, choices=BK_SLOT)
    serviceType = models.CharField(max_length=30)
    SProvider = models.CharField(max_length=30)

    def __str__(self):
        return str(self.bookingDate) + " | Slot - " + str(self.bookingSlot) + " | Service - " +  str(self.serviceType)

class Listing(models.Model):
    Charges = models.IntegerField()
    SERVICE_TYPE = (
        ('T1', 'Type1'),
        ('t2', 'Type2'),
    )
    serviceType = models.CharField(max_length=2, choices=SERVICE_TYPE)
