from django.shortcuts import render
from django.http import HttpResponse

def registration(request):
    return render(request, 'users/registration.html')

def log(request):
    return render(request, 'users/login.html')