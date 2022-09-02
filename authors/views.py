from django.shortcuts import render, redirect
from .forms import AuthorForm, LoginForm, UserRecipeForm
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from home.models import Recipe
from home.pagination_module import PaginationRecipe


def authors(request):
    if request.user.is_authenticated:
        return redirect('authors:login')
    else:
        register = request.session.get('register_form_data', None)
        form = AuthorForm(register)
        context = {
            'form': form
        }

        return render(request, 'register/register_authors.html', context)


def authors_register_post(request):
    if not request.POST:
        raise Http404('Página não encontrada!')
    request.session['register_form_data'] = request.POST

    form = AuthorForm(request.POST)
    if form.is_valid():

        ''' Caso o form seja válido "user_data" recebe os dados do formulário antes do save.
        "set_password" transforma a senha em hash em seguida salva no banco de dados e exibe mensagem de sucesso.
        "del" vai apagar os dados da session ['register_form_data'] pare retornar url para author:register.'''

        user_data = form.save(commit=False)
        user_data.set_password(user_data.password)
        user_data.save()
        messages.success(request, 'Cadastro efetuado com sucesso!')
        del(request.session['register_form_data'])

    return redirect('authors:register')


def login_authenticate(request):
    context = {
        'form': LoginForm()
    }
    return render(request, 'login/login_authors.html', context)


def login_create(request):
    if not request.POST:
        raise Http404('Página não encontrada!')

    form = LoginForm(request.POST)
    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password')
        )

        if authenticated_user is not None:
            login(request, authenticated_user)
            messages.success(request, 'Logado com sucesso!')
        else:
            messages.error(request, 'Usuário ou senha incorreto!')
    else:
        messages.error(request, 'Formulário incorreto')

    return redirect('authors:login')


@login_required(login_url='authors:login', redirect_field_name='next')
def logout_user(request):
    if request.POST:
        logout(request)
        messages.info(request, 'Deslogado com sucesso!')
        return redirect('authors:login')
    else:
        return redirect('authors:login')


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_user(request):
    recipes = Recipe.objects.filter(author=request.user).order_by('pk')
    pag = PaginationRecipe(recipes, request.GET.get('page'))
    context = pag.make_pagination()

    return render(request, 'dashboard/dashboard_authors.html', context)


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_user_category(request, pk):
    recipes = Recipe.objects.filter(author=request.user, recipe_category__pk=pk).order_by('pk')

    pag = PaginationRecipe(recipes, request.GET.get('page'))
    context = pag.make_pagination()

    return render(request, 'dashboard/dashboard_authors.html', context)


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_pending(request):
    recipes = Recipe.objects.filter(author=request.user, active=False).order_by('pk')
    pag = PaginationRecipe(recipes, request.GET.get('page'))
    context = pag.make_pagination()

    return render(request, 'dashboard/dashboard_authors.html', context)


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_approved(request):
    recipes = Recipe.objects.filter(author=request.user, active=True).order_by('pk')
    pag = PaginationRecipe(recipes, request.GET.get('page'))
    context = pag.make_pagination()

    return render(request, 'dashboard/dashboard_authors.html', context)


@login_required(login_url='authors:login', redirect_field_name='next')
def sending_recipe(request):
    register = request.session.get('register_form_data')

    form = UserRecipeForm(register)

    context = {
        'form': form
    }

    return render(request, 'sending_recipe/sending_recipe_authors.html', context)


def sending_recipe_post(request):
    if not request.POST:
        raise Http404('Página não encontrada!')
    request.session['register_form_data'] = request.POST

    form = UserRecipeForm(request.POST, request.FILES)
    if form.is_valid():
        database_form = form.save(commit=False)

        database_form.author = request.user
        database_form.save()

        messages.success(request, 'Sua receita foi enviada com sucesso e será analisada para aprovação em até 2 dias!')

        return redirect('authors:recipe')

    messages.error(request, 'Erro ao enviar formulário')
    return redirect('authors:recipe')


