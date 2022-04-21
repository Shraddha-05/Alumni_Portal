from django.shortcuts import render,  get_object_or_404, redirect, reverse
from django.http import HttpResponse
import csv
from django.contrib.auth.models import User
from .filters import UserFilter
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.views.generic import  CreateView, UpdateView
from django.urls import reverse_lazy
from member.forms import SignUpForm, Register_Form
from .models import Register_Model
# from .models import Company_Model


class UserRegistrationView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('login')


def register_view(request):
    form = Register_Form(request.POST or None, request.FILES or None)
    
    if (request.method == "POST"):
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse("index"))
    
    context = {        
        'form': form
    }
    
    
    return render(request, "tpregister.html", context)



def search(request):
    user_list = Register_Model.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'user_list.html', {'filter': user_filter})

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['first_name','last_name','Email','Branch','Home_Town','Join_Year','Passout_Year','Ph_No','CGPA','Semester','Batch','company_Name','country','city','designation','work_area','Specification','Experience'])

    users = Register_Model.objects.all().values_list('first_name', 'last_name', 'Email','Branch', 'Home_Town', 'Ph_No', 'CGPA', 'Semester', 'Batch')
    for user in users:
        writer.writerow(user)

    return response

