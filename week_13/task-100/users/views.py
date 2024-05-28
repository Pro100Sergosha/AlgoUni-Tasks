from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def user_login(request):
    if request.method =='POST':
        form = UserLoginForm(request.POST)
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
                return redirect('login')
        else:
            return  redirect('login')
    else:
        form = UserLoginForm()
        return render(request, 'users/login.html', {'form':form})


def user_registration(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = UserCreationForm()
    return render(request, 'users/register.html',{'form':form})


def mentor_registration(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'],password=data['password1'])
            user.is_staff = True
            user.save()
            return redirect('index')
    form = UserCreationForm()
    return render(request, 'users/mentor_register.html',{'form':form})



def user_logout(request):
    logout(request)
    return redirect('index')