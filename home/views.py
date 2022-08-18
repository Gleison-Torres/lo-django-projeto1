from django.shortcuts import render, Http404
from . import models
from django.db.models import Q
from django.core.paginator import Paginator
from .pagination_module import PaginationRecipe


def index(request):
    recipes = models.Recipe.objects.filter(active=True).order_by('pk')

    show_pages = 5
    pages = Paginator(recipes, 6)
    if pages.num_pages < 4:
        show_pages = pages.num_pages + 1

    pag = PaginationRecipe(pages, request.GET.get('page'), list(range(1, show_pages)))

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

    show_pages = 5
    pages = Paginator(recipes, 6)
    if pages.num_pages < 4:
        show_pages = pages.num_pages + 1

    pag = PaginationRecipe(pages, request.GET.get('page'), list(range(1, show_pages)))
    context = pag.make_pagination()
    return render(request, 'categories/category.html', context)


def search_recipe(request):
    search_term = request.GET.get('search', '').strip()

    recipes = models.Recipe.objects.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term), active=True).order_by('pk')

    show_pages = 5
    pages = Paginator(recipes, 6)
    if pages.num_pages < 4:
        show_pages = pages.num_pages + 1

    pag = PaginationRecipe(pages, request.GET.get('page'), list(range(1, show_pages)), f'&search={search_term}')
    context = pag.make_pagination()

    return render(request, 'search/search_page.html', context)
