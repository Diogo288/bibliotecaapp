from django.db import models
from livros.models import Livro
from emprestimos.models import Emprestimo

# Create your models here.

class ItemEmprestimo(models.Model):
    quantidade = models.IntegerField('Quantidade', default=1)
    valor_diaria = models.DecimalField('Valor da Diaria', max_digits=10, decimal_places=2, default=0)
    subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, default=0, editable=False)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE, related_name='itens')

    class Meta:
        verbose_name = 'Item de Emprestimo'
        verbose_name_plural = 'Itens de Emprestimo'
        ordering = ['id']

    def save(self, *args, **kwargs):
        self.subtotal = self.quantidade * self.valor_diaria
        super().save(*args, **kwargs)
        total = sum(item.subtotal for item in self.emprestimo.itens.all())
        self.emprestimo.valor_total = total
        self.emprestimo.save()

    def __str__(self):
        return f'{self.livro} - Emprestimo {self.emprestimo.id}'