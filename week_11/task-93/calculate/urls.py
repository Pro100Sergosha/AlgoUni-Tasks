from django.urls import path
from .views import calculate_manager
urlpatterns = [
    path('<str:text>/<int:a>/<int:b>', calculate_manager),
]
