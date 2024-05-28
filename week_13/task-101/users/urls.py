from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('user_register/', views.user_register, name='user_register'),
    path('organisator_register/', views.organisator_register, name='organisator_register'),
]
