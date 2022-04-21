from django.db import models

# Create your models here.
'''
class Adm_Staff(models.Model):
    profile_pic = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=25)
    designation = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    ph_number = models.CharField(max_length=12, null=True, blank=True)
    
    def __str__(self):
        return self.name


class T_P_Staff(models.Model):
    Profile_pic = models.ImageField(null=True, blank=True)
    Name = models.CharField(max_length=25)
    Designation = models.CharField(max_length=50)
    Email = models.EmailField(null=True, blank=True)
    Ph_number = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.Name

class Alumni(models.Model):
    PROFILE_PIC = models.ImageField(null=True, blank=True)
    NAME = models.CharField(max_length=25)
    DESIGNATION = models.CharField(max_length=50)
    BATCH = models.CharField(max_length=12)
    EMAIL = models.EmailField(null=True, blank=True)
    PH_NUMBER = models.CharField(max_length=12, null=True, blank=True)
    FEATURED = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.NAME
'''
