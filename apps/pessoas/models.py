from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    endereco = models.CharField('Endereco', max_length=200)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail', max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'