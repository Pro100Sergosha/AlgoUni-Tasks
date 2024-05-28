from django.urls import path
from .views import index, add_recipe, recipe_info
urlpatterns = [
    path('', index, name='index'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('recipe_info/<str:name>', recipe_info, name='recipe_info'),
]
 
