from django.contrib import admin

# Register your models here.
from .models import Register_Model, Author
# from .models import Company_Model

admin.site.register(Register_Model)
# admin.site.register(Company_Model)