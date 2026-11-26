from django.db import models
from generos.models import Genero

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField('Titulo', max_length=150)
    autor = models.CharField('Autor', max_length=100)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    sinopse = models.TextField('Sinopse', max_length=500)
    data_publicacao = models.DateField('Data de Publicacao')
    paginas = models.IntegerField('Numero de Paginas', default=0)
    preco = models.DecimalField('Preco', max_digits=10, decimal_places=2, default=0)
    disponivel = models.BooleanField('Disponivel', default=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['id']

    def __str__(self):
        return f'{self.titulo}'