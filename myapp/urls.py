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
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('why_us/', views.why_us, name='why_us'),
    path('food_for_all/', views.food_for_all, name='food_for_all'),
    path('zero_food_wastage/', views.zero_food_wastage, name='zero_food_wastage'),
    path('community_fridge/', views.community_fridge, name='community_fridge'),
    path('meals_on_wheele/', views.meals_on_wheele, name='meals_on_wheele'),
    path('our_program/', views.our_program, name='our_program'),
    path('our_donators/', views.our_donators, name='our_donators'),
    path('about_us/', views.about_us, name='about_us'),
    path('donate/', views.donate, name='donate'),
    path('registerView/', views.registerView, name='registerView'),
    path('loginView/', views.loginView, name='loginView'),
    path('logoutView/', views.logoutView, name='logoutView'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
]
