from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is Home page")

def about(request):
    return HttpResponse("This is About page")

def contact(request):
    return HttpResponse("Contact with me by this email prizrakgames21@mail.ru")