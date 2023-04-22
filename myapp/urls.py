"""waste_food_management_and_donation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('why_us/', views.why_us, name='why_us'),
    path('our_program/', views.our_program, name='our_program'),
    path('our_donators/', views.our_donators, name='our_donators'),
    path('about_us/', views.about_us, name='about_us'),
    
    path('registerView/', views.registerView, name='registerView'),
    path('loginView/', views.loginView, name='loginView'),
    path('logoutView/', views.logoutView, name='logoutView'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('food_donation/', views.food_donation, name='food_donation'),
    path('profile/', views.profile, name='profile'),
    path('history/', views.history, name='history'),

    path('reset_password/', views.reset_password, name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),




    
]


