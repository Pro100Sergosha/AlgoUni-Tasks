from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        return render(request, "contact.html", {'email': email})
    return render(request, 'contact.html')
    

def choice(request):
    if request.method == 'POST':
        choice = request.POST.get('choice')
        return redirect(f'{choice}')
    return render(request, 'home.html')

