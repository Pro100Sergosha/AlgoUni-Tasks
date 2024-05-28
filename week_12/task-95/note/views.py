from django.shortcuts import render, redirect
from .models import Note
# Create your views here.

def index(request):
    notes = Note.objects.all()
    return render(request, 'index.html', {'notes':notes})


def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        new_note = Note(
            title=title,
            content=content
        )
        new_note.save()
        return redirect('index')
    return render(request, 'add_note.html')


def note_info(request, title):
    note = Note.objects.get(title=title)
    return render(request, 'note_info.html', {'note':note})


def edit_note(request, title):
    if request.method == 'POST':
        note = Note.objects.get(title=title)
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return render(request,'note_info.html', {'note':note})
    return render(request, 'edit_note.html')

def delete_note(request, title):
    note = Note.objects.get(title=title)
    note.delete()
    return redirect('index')