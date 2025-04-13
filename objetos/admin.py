from django.contrib import admin
from .models import Objeto, Categoria

@admin.register(Categoria)
class CategoriaModelAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Objeto)
class ObjetosModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'status', 'imagem']