from django.shortcuts import render, redirect
from .models import Post, Comment
from django.db import IntegrityError


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'core/index.html', context=context)

def new_comment(request, post_id):
    if request.method == 'POST':
            post = Post.objects.get(id=post_id)
            text = request.POST.get('comment')
            author = request.user
            comment = Comment.objects.create(post=post, text=text, author=author)
    return redirect('core:index')


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
