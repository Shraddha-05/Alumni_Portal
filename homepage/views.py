from django.shortcuts import render

'''
Alumni, Adm_Staff, T_P_Staff
'''
def index(request):
    
    return render(request, 'index.html', {})
