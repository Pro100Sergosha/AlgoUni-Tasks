import random
import string
from django.shortcuts import render, redirect
from .models import Url 
# Create your views here.

def index(request):
    if request.method =='POST':
        url = request.POST.get('new_url')
        new_url = Url(
            long_url=url, 
            short_url = url_shortener())
        new_url.save()
        return redirect('index')
    urls = Url.objects.all()
    return render(request, 'index.html', {'urls':urls})



def url_info(request, id):
    url = Url.objects.get(id=id)
    return render(request,'url_info.html', {'url': url})


def url_shortener():
    characters = string.ascii_letters + string.hexdigits
    rand_url = ''.join([''+random.choice(characters) for _ in range(7)])
    return 'www.ShortUrl.com/' + rand_url


def url_redirection(request, id):
    url = Url.objects.get(id=id)
    url.redirections+=1
    url.save()
    return redirect(url.long_url)