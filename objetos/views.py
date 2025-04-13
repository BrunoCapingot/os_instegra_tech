from django.shortcuts import render
from django.views.generic import ListView
from .models import Objeto


class ObjetosListView(ListView):
    template_name = 'objetos_list.html'
    queryset = Objeto.objects.only('nome', 'imagem')
    context_object_name = 'objetos'