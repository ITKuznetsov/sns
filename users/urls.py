from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.log, name='login'),
    path('myprofile/', views.my_profile, name='myprofile'),
    path('logout/', views.out, name='logout'),
    path('profile/<str:profile_username>/', views.profile, name='profile'),
    path('new-request/<str:profile_username>/', views.friend_request, name='friend_request'),
    path('delete-request/<str:profile_username>/', views.delete_request, name='delete_request'),
    path('accept/<str:profile_username>/', views.accept, name='accept'),
    path('delete/<str:profile_username>/', views.delete, name='delete'),
    path('myfriends/', views.myfriends, name='myfriends'),
]
