from django.db import models

class User(models.Model):
    User_Name = models.CharField(max_length=1000)
    User_Age = models.IntegerField()
    User_CNIC = models.CharField(max_length=13)
    User_Email = models.EmailField(max_length=254)
    User_Password = models.CharField(max_length=64)
    User_Phone = models.IntegerField()
    User_Address = models.CharField(max_length=1000)
    


class ServiceProvider(models.Model):
    SP_Name = models.CharField(max_length=1000)
    SP_Age = models.IntegerField()
    SP_CNIC = models.CharField(max_length=13)
    SP_Email = models.EmailField(max_length=254)
    SP_Password = models.CharField(max_length=64)
    SP_Phone = models.IntegerField()
    SP_Address = models.CharField(max_length=1000)
    SP_ExperienceNo = models.IntegerField()
    SP_ExperienceDetail = models.CharField(max_length=10000)
    SP_Resume = models.FileField()
    
