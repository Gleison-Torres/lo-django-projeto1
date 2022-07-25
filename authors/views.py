from django.shortcuts import render, redirect
from .forms import AuthorForm
from django.http import Http404
from django.contrib import messages


def authors(request):
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

