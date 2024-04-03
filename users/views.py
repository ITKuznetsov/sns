from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate, login, logout  

def registration(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        psw = request.POST.get('psw')
        psw_repeat = request.POST.get('psw_repeat')
        if psw == psw_repeat:
            user = User.objects.create_user(email=email, username=username, password=psw)
            if user is not None:
                login(request, user)
                return redirect('users:profile')
            else:
                message = "Registration's error!"
                return render(request, 'users/registration.html', {'message': message})
    else:
        if request.user.is_authenticated:
            message = "By filling this form you'll create new account!"
            return render(request, 'users/registration.html', {'message': message})
        return render(request, 'users/registration.html')

def log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        psw = request.POST.get('psw')
        user = authenticate(request, username=username, password=psw)
        if user is not None:
            login(request, user)
            return redirect('users:profile')
        else:
            message = "Login's error!"
            return render(request, 'users/login.html', {'message': message}) 
    else:
        if request.user.is_authenticated:
            message = "By filling this form you'll login in another account!"
            return render(request, 'users/login.html', {'message': message})
        return render(request, 'users/login.html')

def profile(request):
    return render(request, 'users/profile.html')

def out(request):
    logout(request)
    return redirect('users:login')