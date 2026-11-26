from django.db import models
from pessoas.models import Pessoa
from redessociais.models import RedeSocial

# Create your models here.

class Leitor(Pessoa):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    matricula = models.CharField('Matricula', max_length=20, unique=True)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField('Data de Nascimento')
    redes_sociais = models.ManyToManyField(RedeSocial, through='LeitorRedeSocial', blank=True)

    class Meta:
        verbose_name = 'Leitor'
        verbose_name_plural = 'Leitores'
        ordering = ['id']

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class LeitorRedeSocial(models.Model):
    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    rede_social = models.ForeignKey(RedeSocial, on_delete=models.CASCADE)
    usuario = models.CharField('Usuario', max_length=100)
    data_vinculo = models.DateField('Data de Vinculo', auto_now_add=True)

    class Meta:
        verbose_name = 'Rede Social do Leitor'
        verbose_name_plural = 'Redes Sociais dos Leitores'
        ordering = ['id']

    def __str__(self):
        return f'{self.leitor} - {self.rede_social}: {self.usuario}'