from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, "generator/home.html")

def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if request.GET.get('numbers'):
        chars += '0123456789'
    if request.GET.get('special'):
        chars += '!@#$%^&*()'
    
    length = int(request.GET.get('length', '12'))
    
    thepassword = ''
    
    for x in range(length):
        thepassword += random.choice(chars)
    
    return render(request, "generator/password.html", {'password' : thepassword})

def about(request):
    return render(request, 'generator/about.html')
