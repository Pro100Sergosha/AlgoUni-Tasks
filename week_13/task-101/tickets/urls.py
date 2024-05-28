from django.urls import path
from tickets import views
urlpatterns = [
    path('', views.index, name='index')
]
