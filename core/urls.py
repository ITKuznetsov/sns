from django.urls import path
from . import views

app_name='core'
urlpatterns = [
    path('', views.index, name='index'),
    path('new-post', views.new_post, name='new-post'),
    path('new-comment/<int:post_id>/', views.new_comment, name='new-comment'),
    path('like/<int:post_id>/', views.like, name='like'),
    path('dislike/<int:post_id>/', views.dislike, name='dislike'),
    path('un/<int:post_id>/', views.superUn, name='superUn'),
]
