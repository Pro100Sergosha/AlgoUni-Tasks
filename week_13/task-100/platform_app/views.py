from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CourseForm
from .models import Course
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def index(request):
    courses = Course.objects.all()
    return render(request, 'platform/index.html', {'courses': courses})

def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'platform/list_courses.html', {'courses': courses})

def add_course(request, id):
    if request.method == 'POST':
        category = request.POST.get('category')
        form = CourseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            course = Course(title=data['title'], description=data['description'], category=data['category'])
            course.created_by = User(id=id)
            course.save()
            return redirect('index')
    form = CourseForm()
    return render(request, 'platform/add_course.html', {'form':form})

def favourite(request):
    currentuser = request.user
    course = currentuser.favourite.all()
    return render(request, 'platform/favourite.html', {'favourite':course})

def add_favourite(request, id):
    list_course = Course.objects.get(id=id)
    current_user = request.user
    list_course.favourite.add(current_user)
    return redirect('index')

def delete_favourite(request, id):
    course = Course.objects.get(id=id)
    current_user = request.user
    course.favourite.remove(current_user)
    return redirect('favourite')

def edit_course(request, id):
    course = Course.objects.get(id=id)
    if request.method =='POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm(instance=course)
        return render(request, 'platform/add_course.html', {'form':form})

def info_course(request, id):
    course = Course.objects.get(id=id)
    return render(request,'platform/info_course.html', {'course':course})

def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('index')


