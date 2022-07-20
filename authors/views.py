from django.shortcuts import render, redirect
from .forms import AuthorForm
from django.http import Http404
from django.contrib import messages


def authors(request):
    register = request.session.get('register_form_data', None)
    print(register)
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
        form.save()
        messages.success(request, 'Cadastro efetuado com sucesso!')
        del(request.session['register_form_data'])

    return redirect('authors:register')

