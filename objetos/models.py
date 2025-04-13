from django.db import models
from stdimage import StdImageField


class Categoria(models.Model):
    nome = models.CharField('nome', max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Objeto(models.Model):
    DISPONIVEL = 'dis'
    INDISPONIVEL = 'ind'
    MANUTENCAO = 'man'

    OBJETO_STATUS_CHOICES = (
        (DISPONIVEL, 'Disponível'),
        (INDISPONIVEL, 'Indisponível'),
        (MANUTENCAO, 'Manutenção')
    )

    nome = models.CharField('nome', max_length=100)
    descricao = models.TextField('descrição', blank=True, null=True)
    status = models.CharField('status do item', max_length=3, default=DISPONIVEL)
    categoria = models.ForeignKey(Categoria, related_name='objeto_categoria', on_delete=models.CASCADE)
    imagem = StdImageField(
        upload_to='objects',
        variations={
            'thumb': (300, 300, True),  # largura, altura, crop (cortar)
            'medium': (600, 400),
        }
    )

    def __str__(self):
        return f'{self.nome} - {self.status}'