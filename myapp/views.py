from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Restaurant, NGO



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

# @login_required(redirect_field_name='loginView',login_url='loginView')
# def dashboard(request):
#     return render(request, 'dashboard.html', locals())

@login_required(redirect_field_name='loginView',login_url='loginView')
def dashboard(request):
    return render(request, 'dashboard1.html', locals())

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
