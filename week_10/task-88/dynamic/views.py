from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, name):
    return HttpResponse(f"Hello, {name}")