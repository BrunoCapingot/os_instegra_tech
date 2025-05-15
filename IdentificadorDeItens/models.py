from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Item(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    ano_fabricacao = models.IntegerField()
    fabricante = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem_url = models.CharField(max_length=500)  # ou models.URLField()
    data_aquisicao = models.DateField()
    estado_conservacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
