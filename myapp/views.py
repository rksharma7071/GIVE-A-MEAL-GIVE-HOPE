from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def why_us(request):
    return render(request, 'why_us.html')

def food_for_all(request):
    return render(request, 'food_for_all.html')

def zero_food_wastage(request):
    return render(request, 'zero_food_wastage.html')

def community_fridge(request):
    return render(request, 'community_fridge.html')

def meals_on_wheele(request):
    return render(request, 'meals_on_wheele.html')

def our_program(request):
    return render(request, 'our_program.html')

def our_donators(request):
    return render(request, 'our_donators.html')

def about_us(request):
    return render(request, 'about_us.html')

def donate(request):
    return render(request, 'donate.html')

@login_required(redirect_field_name='loginView',login_url='loginView')
def dashboard(request):
    return render(request, 'dashboard.html', locals())

def loginView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user  = authenticate(request, username=username, password=password)
        if user is None:
            error = 'yes'
        else:
            login(request, user)
            error = 'no'
            return redirect('dashboard')
    return render(request, 'login.html', locals())

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
            first_name = request.POST.get('first_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password == confirm_password:
                try:
                    user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name)
                    messages.success(request, 'Your account has been created!')
                    return redirect('dashboard')
                except Exception as e:
                    messages.error(request, f'{e}')
            else:
                messages.error(request, 'Passwords do not match')
    return render(request, 'register.html', locals())


def logoutView(request):
    logout(request)
    return render('home')

