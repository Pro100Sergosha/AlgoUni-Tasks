from django.shortcuts import render, redirect
from .models import Recipe
# Create your views here.


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes':recipes})



def add_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
        new_recipe = Recipe(
            name = name,
            ingredients = ingredients,
            instructions = instructions,
        )
        new_recipe.save()
        return redirect('index')
    return render(request, 'add_recipe.html')


def recipe_info(request, name):
    recipe = Recipe.objects.get(name=name)
    return render(request, 'recipe_info.html', {'recipe':recipe})