from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.log, name='login'),
    path('myprofile/', views.my_profile, name='myprofile'),
    path('logout/', views.out, name='logout'),
    path('profile/<str:profile_username>/', views.profile, name='profile'),
]
