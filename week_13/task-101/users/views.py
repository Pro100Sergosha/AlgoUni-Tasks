from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
# Create your views here.

def user_login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data is not None:
                user = authenticate(request, username=data['username'], password=data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('index')
                else:
                    return redirect('login')
    else: 
        form = LoginForm()
        return render(request, 'users/login.html', {'form':form})



def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = UserCreationForm(request.POST)
    return render(request, 'users/user_register.html', {'form':form})

def organisator_register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'], password=data['password1'])
            user.is_staff = True
            user.save()
            return redirect('index')
    form = UserCreationForm()
    return render(request, 'users/organisator_register.html', {'form':form})