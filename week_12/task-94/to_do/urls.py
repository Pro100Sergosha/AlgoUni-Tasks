from django.urls import path
from .views import index, add_event, event_info, edit_event, delete_event
urlpatterns = [
    path('', index, name='index'),
    path('addevent', add_event, name='addevent'),
    path('edit/<str:title>', edit_event, name='edit_event'),
    path('delete/<str:title>', delete_event, name='delete_event'),
    path('info/<str:title>', event_info, name='event_info'),
]
