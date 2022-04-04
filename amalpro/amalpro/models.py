from django.db import models

class User(models.Model):
    User_Name = models.CharField(max_length=1000)
    User_Age = models.IntegerField()
    User_CNIC = models.IntegerField()
    User_Email = models.EmailField(max_length=254)
    User_Password = models.CharField(max_length=64)
    User_Phone = models.IntegerField()
    User_Address = models.CharField(max_length=1000)
    USER_TYPE = (
        ('C', 'Customer'),
        ('SP', 'Service Provider')
    )
    Usertype = models.CharField(max_length=2, choices=USER_TYPE)

class Customer(models.Model):
    Fullname = models.CharField(max_length=1000)
    CNIC = models.IntegerField()
    Address = models.CharField(max_length=1000)
    City = models.CharField(max_length=1000)
    Dateofbirth = models.DateTimeField(auto_now=True)
    Reviews = models.CharField(max_length=10000)

class Transaction(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    debit = models.IntegerField()
    credit = models.IntegerField()

class Purchases(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    debit = models.IntegerField()
    credit = models.IntegerField()

class ServiceProvider(models.Model):
    Fullname = models.CharField(max_length=1000)
    CNIC = models.IntegerField()
    Address = models.CharField(max_length=1000)
    City = models.CharField(max_length=1000)
    Dateofbirth = models.DateTimeField(auto_now=True)
    # Checkbox
    LANG = (
        ('PK', 'Urdu'),
        ('EN', 'English')
    )
    Language = models.CharField(max_length=2, choices=STAT)
    ExperienceNo = models.IntegerField()
    SERVICETYPE =(
        ('A','A')
    )
    ServiceType = models.CharField(max_length=1, choices=SERVICETYPE)
    SLOTS =(
        ('A','A')
    )
    Slots = models.CharField(max_length=1, choices=SLOTS)
    Reviews = models.CharField(max_length=10000)

class ServiceProvider(models.Model):
    SP_Name = models.CharField(max_length=1000)
    SP_Age = models.IntegerField()
    SP_CNIC = models.IntegerField()
    SP_Email = models.EmailField(max_length=254)
    SP_Password = models.CharField(max_length=64)
    SP_Phone = models.IntegerField()
    SP_Address = models.CharField(max_length=1000)
    SP_ExperienceNo = models.IntegerField()
    SP_ExperienceDetail = models.CharField(max_length=10000)
    SP_Resume = models.FileField()

class Listing(models.Model):
    Name = models.CharField(max_length=1000)
    CNIC = models.IntegerField()
    Charges = models.IntegerField()
    SERVICE_TYPE = (
        ('A', 'A')
    )
    userType = models.CharField(max_length=1, choices=SERVICE_TYPE)


class Service(models.Model):
    SERVICE_TYPE = (
        ('1', 'Cleaning'),
        ('2', 'Painting'),
        ('3', 'Gardening'),
        ('4', 'Construction'),
        ('5', 'Plumbing'),
        ('6', 'Mechanic'),
        ('7', 'Electrician'),
        ('8', 'Nurse'),
        ('9', 'Chef'),
        ('10', 'Babysitter')
    )
    userType = models.CharField(max_length=1, choices=SERVICE_TYPE)







