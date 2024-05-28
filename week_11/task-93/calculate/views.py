from django.shortcuts import render

# Create your views here.
def calculate_manager(request, text, a, b):
    if text == 'add':
        x = a+b
        return render(request, 'index.html', {'calculate':x})
    elif text == 'substract':
        x = a-b
        return render(request, 'index.html', {'calculate':x})
    elif text == 'multiply':
        x = a*b
        return render(request, 'index.html', {'calculate':x})
    elif text == 'divide':
        x = a/b
        return render(request, 'index.html', {'calculate':x})
