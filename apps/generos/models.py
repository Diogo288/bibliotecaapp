from django.db import models

# Create your models here.
class Genero(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=200)
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.nome}'