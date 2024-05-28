from django.urls import path
from .views import user_login, user_registration, user_logout, mentor_registration

urlpatterns = [
    path('login/', user_login, name='login'),
    path('user_register/', user_registration, name='user_register'),
    path('mentor_register/', mentor_registration, name='mentor_register'),
    path('logout/', user_logout, name='logout'),
]
