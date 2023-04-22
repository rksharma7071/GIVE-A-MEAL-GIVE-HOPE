from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Restaurant, NGO
from .forms import *
from django.core.mail import send_mail
from django.contrib.auth import views as auth_views
from django.http import HttpResponse


def home(request): 
    return render(request, 'home.html')


def why_us(request):
    return render(request, 'why_us.html')


def our_program(request):
    return render(request, 'our_program.html')


def our_donators(request):
    return render(request, 'our_donators.html')


def about_us(request):
    return render(request, 'about_us.html')


@login_required(redirect_field_name='loginView',login_url='loginView')
def dashboard(request):    
    return render(request, 'dashboard.html', locals())


def loginView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':

        username = request.POST.get('email')
        password = request.POST.get('password')
        
        if checkbox := request.POST.get('terms'):
            try:
                user  = authenticate(request, username=username, password=password)
                if user is None:
                    messages.error(request, 'Your username and password is incorrect.')

                else:
                    login(request, user)
                    return redirect('dashboard')
            except Exception as e:
                messages.error(request, f'{e}')
        else:
            messages.error(request, 'Please indicate that you accept the Terms and Conditions.')
    return render(request, 'login.html', locals())


login_required(redirect_field_name='loginView', login_url='loginView')
def logoutView(request):
    logout(request)
    return redirect('home')


def registerView(request):
    if request.method == 'POST':
        organization = request.POST['organization']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        terms = request.POST.get('terms')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('registerView')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('registerView')

        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name)
        user.save()

        if organization == '1':
            group = Group.objects.get(name='ngo')
            user.groups.add(group.id)
            ngo = NGO(user=user)
            ngo.save()

        elif organization == '2':
            group = Group.objects.get(name='restaurant')
            user.groups.add(group.id)
            restaurant = Restaurant(user=user)
            restaurant.save()
            
        elif organization == '3':
            group = Group.objects.get(name='donator')
            user.groups.add(group.id)
            donator = donator(user=user)
            donator.save()

        messages.success(request, 'Account created successfully!')
        return redirect('loginView')

    return render(request, 'registerView.html')


def food_donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food Donation placed successfully!')
            return redirect('food_donation')
    else:
        form = DonationForm()

    return render(request, 'food_donation.html', locals())


@login_required(redirect_field_name='loginView',login_url='loginView')
def donation_record(request):
    pass


def profile(request):
    return render(request, 'profile.html')


def history(request):
    ngo = request.user.groups.filter(name='ngo').exists
    donator = request.user.groups.filter(name='donator').exists

    donations = Donation.objects.all().order_by('-created_at')
    return render(request, 'history.html', locals())


def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        users = User.objects.filter(email=email)
        if users.exists():
            for user in users:
                send_mail('Reset Your Password',f'Follow this link to reset your password: http://localhost:8000/reset/{str(user.pk)}/','rksharma7071@gmail.com',[email],fail_silently=False,)
            messages.success(request, 'Password reset email has been sent')
        else:
            messages.error(request, 'User does not exist')
    return render(request, 'reset_password.html')


def password_reset_confirm(request, uidb64, token):
    return auth_views.PasswordResetConfirmView.as_view()(request, uidb64=uidb64, token=token, template_name='password_reset_confirm.html')

