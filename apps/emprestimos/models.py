from django.db import models
from leitores.models import Leitor
from bibliotecarios.models import Bibliotecario

# Create your models here.

class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('ABERTO', 'Aberto'),
        ('DEVOLVIDO', 'Devolvido'),
        ('ATRASADO', 'Atrasado'),
    ]
    data_emprestimo = models.DateTimeField('Data do Emprestimo', auto_now_add=True)
    data_devolucao = models.DateField('Data de Devolucao')
    status = models.CharField('Status', max_length=10, choices=STATUS_CHOICES, default='ABERTO')
    valor_total = models.DecimalField('Valor Total', max_digits=10, decimal_places=2, default=0)
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    bibliotecario = models.ForeignKey(Bibliotecario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'
        ordering = ['id']

    def __str__(self):
        return f'Emprestimo {self.id} - {self.leitor}'