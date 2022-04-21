from .models import Register_Model
# from .models import Company_Model
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Register_Model
        fields = ['first_name', 'last_name', 'Branch', 'Home_Town','Join_Year','Passout_Year','Ph_No', 'CGPA', 'Semester', 'Batch','company_Name','country','city','designation','work_area','Specification','Experience' ]

# class UserFilter2(django_filters.FilterSet):
#     class Meta:
#         model = Company_Model
#         fields = ['company_Name','country','city','designation','work_area','Specification','Experience']