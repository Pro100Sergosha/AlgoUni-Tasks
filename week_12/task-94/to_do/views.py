from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
# Create your views here.
def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events':events})

def add_event(request):
    try:
        if request.method == 'POST':
            new_event = Event(
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            date = request.POST.get('date'),
            location = request.POST.get('location'),
            )
            new_event.save()
            return redirect('index')
        return render(request,'add_event.html') 
    except:
        return HttpResponse('Write')


def event_info(request, title):
    event = Event.objects.get(title=title)
    return render(request, 'event_info.html', {'event': event})


def edit_event(request, title):
    if request.method =="POST":
        event = Event.objects.get(title=title)
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.date = request.POST.get('date')
        event.location = request.POST.get('location')
        event.save()
        return redirect('index')
    return render(request, 'edit_event.html')
        
def delete_event(request, title):
    event = Event.objects.get(title=title)
    event.delete()
    return redirect('index')