from django.urls import path
from .views import index, url_info, url_redirection
urlpatterns = [
    path('', index, name='index'),
    path('url_info/<int:id>', url_info, name='url_info'),
    path('url_redirection/<int:id>', url_redirection, name='url_redirection'),
]
