from django.contrib import admin
from django.urls import path
from taskbunny.views import login_view, signup_view, home_view, profile_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('', home_view, name='home'),
]
