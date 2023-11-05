from django.db import models
from django.conf import settings
from datetime import datetime    

# Create your models here.
class Categoria(models.Model) :
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    nome = models.CharField(max_length=250, null=False)
    data_criacao = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.nome

class Hobby(models.Model):
    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'
    
    nome = models.CharField(max_length=250, null=False)
    local = models.CharField(max_length=250, null=False)
    data = models.DateField(null=False)
    time = models.TimeField(null=False)
    imagem = models.ImageField(upload_to='hobby', null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.TextField(null=False)
    # Criador do Hobby
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    def __str__(self):
        return self.nome
    
class Participante(models.Model):
    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'

    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE, related_name='participantes')
    user_participante =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    


