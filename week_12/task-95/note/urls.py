from django.urls import path
from .views import index, add_note, note_info, edit_note, delete_note
urlpatterns = [
    path('', index, name='index'),
    path('add_note/', add_note, name='add_note'),
    path('note_info/<str:title>', note_info, name='note_info'),
    path('edit_note/<str:title>', edit_note, name='edit_note'),
    path('delete_note/<str:title>', delete_note, name='delete_note'),
]
