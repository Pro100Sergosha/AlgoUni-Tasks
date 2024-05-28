from django.urls import path
from .views import choice, contact

urlpatterns = [
    path('', choice),
    path('contact/', contact, name='contact'),
]
