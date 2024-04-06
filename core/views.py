from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import Post
from django.db import IntegrityError

def index(request):
    return render(request, 'core/index.html')

def new_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            text = request.POST.get('text')
            image = request.FILES.get('image')
            user = request.user
            try:
                post = Post.objects.create(text=text, image=image, author=user)
            except IntegrityError:
                error = 'Creation failed'
                return render(request, 'core/new-post.html', {'error': error})
        return render(request, 'core/new-post.html')
    else:
        return redirect('core:index')
