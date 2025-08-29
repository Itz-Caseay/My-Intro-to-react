from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User, Admin, Client
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'index.html')

def adminhome(request):
    return render(request, 'admin.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'client':
                    return redirect('home')
                elif user.user_type == 'admin':
                    return redirect('adminhome')
                
               

            else:
                messages.error(request, 'Les Infos ne correspondents pas')
                return redirect('signin')

        except Exception as e:
            messages.error(request, {'error':e})
    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        role = request.POST.get('role')


        if password == password2:
            if User.objects.filter(email=email, phone=phone, username=username).exists():
                messages.error(request, 'Ceux infos on etais deja pris')
                return redirect('signup')

            else:
                user=User.objects.create_user(email=email, phone=phone, username=username, password=password, user_type=role)
                login(request, user)
                if role == 'admin':
                    Admin.objects.create(user=user)
                    messages.success(request, 'Compte creer avec success attendez vous fais valider')
                    return redirect('adminhome')

                
                elif role == 'client':
                    messages.success(request, 'Compte creer avec success')
                    return redirect('home')

                
        else:
            messages.error(request, 'Les mots de passe ne correspond pas')
            return redirect('signup')

    return render(request, 'signup.html')