from django.db import models
from emprestimos.models import Emprestimo

# Create your models here.

class Recibo(models.Model):
    numero = models.CharField('Numero', max_length=20, unique=True)
    data_emissao = models.DateField('Data de Emissao', auto_now_add=True)
    observacoes = models.TextField('Observacoes', max_length=300, blank=True)
    emprestimo = models.OneToOneField(Emprestimo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Recibo'
        verbose_name_plural = 'Recibos'
        ordering = ['id']

    def __str__(self):
        return f'Recibo {self.numero}'