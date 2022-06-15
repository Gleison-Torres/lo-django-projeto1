from django.shortcuts import render
from . import models


def index(request):
    context = {'recipes': models.Receita.objects.filter(active=True)}
    return render(request, 'home/home.html', context)


def recipe(request, pk):
    context = {'recipe': models.Receita.objects.get(id=pk, active=True)}
    return render(request, 'recipe_page/recipe_page.html', context)


def category_recipe(request, pk):
    context = {'recipes': models.Receita.objects.filter(recipe_category__pk=pk, active=True)}
    return render(request, 'categories/category.html', context)
