from django import forms
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Register_Model



class SignUpForm(UserCreationForm):
    email               = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name          = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name           = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))                
    captcha             = ReCaptchaField()

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] =  'form-control'
        self.fields['password1'].widget.attrs['class'] =  'form-control'
        self.fields['password2'].widget.attrs['class'] =  'form-control'


class EditProfileForm(UserChangeForm):
    email       = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username  = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    captcha = ReCaptchaField()

    class Meta():
        model = User
        fields = ('username', 'email')




class Register_Form(forms.ModelForm):
    class Meta:
        model = Register_Model
        fields = ('first_name','last_name','Email','Branch','Home_Town','Join_Year','Passout_Year','Ph_No','CGPA','Semester','Batch','company_Name','country','city','designation','work_area','Specification','Experience')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'Email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'Branch' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: E.C.E. or C.E.'}),
            'Ph_No': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'CGPA': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Previous Year Cgpa'}),
            'Home_Town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example:City Name Only'}),
            'Join_Year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example:DD/MM/YY' }),
            'Passout_Year': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Example:DD/MM/YY' }),
            'Semester': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1;2;3;4;5;6;7;8'}),
            'Batch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example:20xx-20xx'}),
            'company_Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Company Name'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Current Country'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Current City'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Designation'}),
            'work_area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Work Area'}),
            'Specification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Specification'}),
            'Experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experience In Years'}),
        }
#class Register_Company(forms.ModelForm):
#    class Meta:
#        model = Company_Model
#        fields = ('company_Name','country','city','designation','work_area','Specification','Experience')
#
#        widgets = {
#            'company_Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Company Name'}),
#            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Current Country'}),
#            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Current City'}),
#            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Designation'}),
#            'work_area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Work Area'}),
#            'specification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Specification'}),
#            'Experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experience In Years'}),
#
#        }