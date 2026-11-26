from django.db import models
from pessoas.models import Pessoa

# Create your models here.

class Bibliotecario(Pessoa):
    TURNO_CHOICES = [
        ('M', 'Manha'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
    ]
    salario = models.DecimalField('Salario', max_digits=10, decimal_places=2, default=0)
    cargo = models.CharField('Cargo', max_length=50)
    data_admissao = models.DateField('Data de Admissao')
    turno = models.CharField('Turno', max_length=1, choices=TURNO_CHOICES)

    class Meta:
        verbose_name = 'Bibliotecario'
        verbose_name_plural = 'Bibliotecarios'
        ordering = ['id']

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'