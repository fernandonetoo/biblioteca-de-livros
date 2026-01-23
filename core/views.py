from django.shortcuts import render
from .models import *
# Create your views here.

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'core/lista_filmes.html', {
        'filmes': filmes
    })
