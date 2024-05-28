from django.shortcuts import render, HttpResponse

# Create your views here.
def odd_or_even(request, number):
    if number % 2 == 0:
        return HttpResponse("This number is even.")
    else:
        return HttpResponse("This number  is odd.")