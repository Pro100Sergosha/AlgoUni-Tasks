from django.shortcuts import render, redirect

# Create your views here.

def result(request):
    if request.method == 'POST':
        noun = request.POST.get('noun')
        verb = request.POST.get('verb')
        adjective = request.POST.get('adjective')
        adverb = request.POST.get('adverb')
        return render(request, 'result.html', {'noun':noun, 'verb':verb, 'adjective':adjective, 'adverb':adverb})
    return render(request,'index.html')