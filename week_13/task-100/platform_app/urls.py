from django.urls import path
from platform_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_courses', views.list_courses, name='list_courses'),
    path('add_course/<int:id>', views.add_course, name='add_course'),
    path('edit_course/<int:id>', views.edit_course, name='edit_course'),
    path('delete_course/<int:id>', views.delete_course, name='delete_course'),
    path('info_course/<int:id>', views.info_course, name='info_course'),
    path('favourite/', views.favourite, name='favourite'),
    path('add_favourite/<int:id>', views.add_favourite, name='add_favourite'),
    path('delete_favourite/<int:id>', views.delete_favourite, name='delete_favourite'),
]
