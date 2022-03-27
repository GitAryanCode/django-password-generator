import re
from django.shortcuts import render
from django.http import HttpResponse
import random as rd

from numpy import character 

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get('uppercase'):
        characters.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    if request.GET.get('special'):
        characters.extend("!@#$%&'()*+,-./'")
    
    if request.GET.get('numbers'):
        characters.extend("1234567890")

    length = int(request.GET.get('length', 10))

    password = ""

    for x in range(length):
        password += rd.choice(characters)

    return render(request, 'generator/password.html', {"password":password})

def about(request):
    return render(request, 'generator/about.html')

