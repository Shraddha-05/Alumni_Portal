from tokenize import Name
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from pytz import country_names

User                = get_user_model()

class Author(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username


class Register_Model(models.Model):
    author               = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name           = models.CharField(max_length=120)
    last_name            = models.CharField(max_length=120)
    Home_Town            = models.CharField(max_length=120)
    Join_Year            = models.CharField(max_length=120)
    Passout_Year         = models.CharField(max_length=120)
    Ph_No                = models.CharField(max_length=120)
    CGPA                 = models.CharField(max_length=120)
   # Percentage_in_10th   = models.CharField(max_length=120)
   # Percentage_in_12th   = models.CharField(max_length=120)
    Branch               = models.CharField(max_length=120)
    Semester             = models.IntegerField()
    Batch                = models.CharField(max_length=120)
    Email                = models.EmailField()
    company_Name         = models.CharField(max_length=120)
    country              = models.CharField(max_length=120)
    city                 = models.CharField(max_length=120)
    designation          = models.CharField(max_length=120)
    work_area            = models.CharField(max_length=120)
    Specification        = models.CharField(max_length=120)
    Experience           = models.IntegerField()

# class Company_Model(models.Model):
#     company_Name         = models.CharField(max_length=120)
#     country              = models.CharField(max_length=120)
#     city                 = models.CharField(max_length=120)
#     designation          = models.CharField(max_length=120)
#     work_area            = models.CharField(max_length=120)
#     Specification        = models.CharField(max_length=120)
#     Experience           = models.IntegerField(max_length=10)
# 
    def __str__(self):
        return self.first_name