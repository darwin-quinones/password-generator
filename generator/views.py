from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

import random


def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

# password generator

def password(request):
    
    characters = list('abcdfghijklmnopqrstuvwxyz')
    
    password_length = int(request.GET.get('length'))
    
    generated_password = ''
    
    # Si tiene uppercase de agreag una lsita mas grande
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDFGHIJKLMNOPQRSTUVWXYZ')) 
    if request.GET.get('special'):
        characters.extend(list("!#$%&()*+./:?"))
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    
    for x in range(password_length):
        generated_password += random.choice(characters)
    
    return  render(request, 'generator/password.html', {'password':generated_password})
