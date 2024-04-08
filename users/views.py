from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate, login, logout

def profile(request, profile_username):
    profile = User.objects.get(username=profile_username)
    return render(request, 'users/profile.html', {'profile': profile})

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
                return redirect('users:myprofile')
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
            return redirect('users:myprofile')
        else:
            message = "Login's error!"
            return render(request, 'users/login.html', {'message': message}) 
    else:
        if request.user.is_authenticated:
            message = "By filling this form you'll log in in another account!"
            return render(request, 'users/login.html', {'message': message})
        return render(request, 'users/login.html')

def my_profile(request):
    user = request.user
    posts = user.posts
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('psw')
        first_name = request.POST.get('fn')
        last_name = request.POST.get('ln')
        avatar = request.FILES.get('avatar')

        if email:
            user.email = email
        if username:
            user.username = username
        if password:
            user.set_password(password)
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if avatar:
            user.avatar = avatar

        if any([email, username, password, first_name, last_name, avatar]):
            user.save()

        if password:
            login(request, user)

        return redirect('users:myprofile')

    return render(request, 'users/myprofile.html', {'user': user, 'posts': posts})

def out(request):
    logout(request)
    return redirect('users:login')