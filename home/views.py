from django.shortcuts import render, Http404
from . import models
from django.db.models import Q
from .pagination_module import PaginationRecipe


def index(request):
    recipes = models.Recipe.objects.filter(active=True).order_by('pk')
    pag = PaginationRecipe(recipes, request.GET.get('page'))
    context_page = pag.make_pagination()
    return render(request, 'home/home.html', context_page)


def recipe(request, pk):
    try:
        context = {'recipe': models.Recipe.objects.get(id=pk, active=True)}
    except Exception:
        raise Http404('Página não existe ou receita ainda não foi aprovada pela administração!')
    return render(request, 'recipe_page/recipe_page.html', context)


def category_recipe(request, pk):
    recipes = models.Recipe.objects.filter(recipe_category__pk=pk, active=True).order_by('pk')
    pag = PaginationRecipe(recipes, request.GET.get('page'))
    context = pag.make_pagination()
    return render(request, 'categories/category.html', context)


def search_recipe(request):
    search_term = request.GET.get('search', '').strip()

    recipes = models.Recipe.objects.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term), active=True).order_by('pk')

    pag = PaginationRecipe(recipes, request.GET.get('page'), f'&search={search_term}')
    context = pag.make_pagination()

    return render(request, 'search/search_page.html', context)
