from django.shortcuts import render
from . import models


def index(request):
    context = {'recipes': models.Receita.objects.all()}
    return render(request, 'home/home.html', context)


def recipe(request, pk):

    context = {
        'recipe': models.Receita.objects.get(id=pk)
    }

    return render(request, 'recipe_page/recipe_page.html', context)
