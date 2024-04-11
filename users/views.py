from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from .models import User, FriendRequest
from django.contrib.auth import authenticate, login, logout

def delete_request(request, profile_username):
    if request.method == 'POST':
        user = request.user
        friend = User.objects.filter(username=profile_username).first()
        request = FriendRequest.objects.filter(from_user=user.id, to_user=friend.id)
        request.delete()
        return redirect('users:profile', profile_username=profile_username)

def friend_request(request, profile_username):
    if request.method == 'POST':
        user = request.user
        profile = User.objects.get(username=profile_username)
        request = FriendRequest.objects.create(from_user=user, to_user=profile)
        request.save()
        if request is not None:
            request.save()
            return redirect('users:profile', profile_username=profile_username)
        else:
            # message = "Request's error!"
            return render(request, 'users/myfriends.html')
        

def accept(request, profile_username):
    if request.method == 'POST':
        from_user = User.objects.get(username = profile_username)
        to_user = request.user
        friend_request = FriendRequest.objects.filter(from_user=from_user.id, to_user=to_user.id).first()
        if friend_request:
            friend_request.delete()
            from_user.friends.add(to_user)
            to_user.friends.add(from_user)
        return redirect('users:myfriends')

def delete(request, profile_username):
    if request.method == 'POST':
        user = request.user
        friend = User.objects.filter(username=profile_username).first()
        user.friends.remove(friend)
        friend.friends.remove(user)
        return redirect('users:myfriends')

def myfriends(request):
    user = request.user
    context = {
        'friend_requests': FriendRequest.objects.filter(to_user=user.id),
    }
    return render(request, 'users/myfriends.html', context=context)

def profile(request, profile_username):
    user = request.user
    context = {
    'profile': User.objects.get(username=profile_username),
    'requests': FriendRequest.objects.all(),
    }
    return render(request, 'users/profile.html', context=context)

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