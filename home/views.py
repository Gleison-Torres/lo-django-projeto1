from django.shortcuts import render, Http404
from . import models
from django.db.models import Q
from django.core.paginator import Paginator
from .pagination_module import PaginationRecipe


def index(request):
    recipes = models.Recipe.objects.filter(active=True).order_by('pk')

    pag = PaginationRecipe(Paginator(recipes, 6), request.GET.get('page'), list(range(1, 5)))
    context = pag.make_pagination()

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


def search_recipe(request):
    search_term = request.GET.get('search', '').strip()
    context = {
        'recipes': models.Recipe.objects.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term), active=True)
    }
    return render(request, 'search/search_page.html', context)

