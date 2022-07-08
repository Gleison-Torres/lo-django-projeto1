from django.shortcuts import render
from .forms import AuthorForm


def authors(request):
    form = AuthorForm
    context = {'form': form}
    return render(request, 'register/register_authors.html', context)

