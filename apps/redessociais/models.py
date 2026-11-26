from django.db import models

# Create your models here.

class RedeSocial(models.Model):
    nome = models.CharField('Nome', max_length=50)
    tipo_conteudo = models.TextField('Tipo de Conteudo', max_length=200)
    url = models.URLField('URL', max_length=200)
    ativa = models.BooleanField('Ativa', default=True)

    class Meta:
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'
        ordering = ['id']

    def __str__(self):
        return f'{self.nome}'