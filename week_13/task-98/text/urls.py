from django.urls import path
from .views import index, add_text, text_info, edit_text

urlpatterns = [
    path('', index, name='index'),
    path('add_text/', add_text, name='add_text'),
    path('info/<int:id>', text_info, name='text_info' ),
    path('info/edit_text/<int:id>', edit_text, name='edit_text')
]
