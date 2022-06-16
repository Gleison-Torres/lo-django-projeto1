from django.shortcuts import render, Http404
from . import models


def index(request):
    context = {'recipes': models.Recipe.objects.filter(active=True)}
    return render(request, 'home/home.html', context)


def recipe(request, pk):
    try:
        context = {'recipe': models.Recipe.objects.get(id=pk, active=True)}
    except Exception:
        raise Http404()

    return render(request, 'recipe_page/recipe_page.html', context)


def category_recipe(request, pk):

    context = {
        'recipes': models.Recipe.objects.filter(recipe_category__pk=pk, active=True),
        'title': models.Recipe.objects.filter(recipe_category__pk=pk).first().recipe_category
    }

    return render(request, 'categories/category.html', context)
