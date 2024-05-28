from django.shortcuts import render, redirect
from .models import Text
from .forms import TextForm

def index(request):
    texts = Text.objects.all()
    return render(request, 'index.html', {'texts':texts})


def add_text(request):
    if request.method == 'POST':
        form = TextForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TextForm()
        return render(request, 'add_text.html', {'form':form})


def text_info(request, id):
    text = Text.objects.get(id=id)
    return render(request, 'text_info.html', {'text':text})

def edit_text(request, id):
    text = Text.objects.get(pk=id)
    if request.method == 'POST':
        form = TextForm(request.POST, request.FILES, instance=text)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TextForm(instance=text)
        return render(request, 'add_text.html',{'form':form})
