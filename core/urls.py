from django.urls import path
from . import views

app_name='core'
urlpatterns = [
    path('', views.index, name='index'),
    path('new-post', views.new_post, name='new-post'),
    path('new-comment/<int:post_id>/', views.new_comment, name='new-comment'),
]
