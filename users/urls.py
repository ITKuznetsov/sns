from django.urls import path
from . import views

app_name='users'
urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.log, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.out, name='logout')
]
