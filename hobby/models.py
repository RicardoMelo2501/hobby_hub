from django.db import models

# Create your models here.
class Hobby(models.Model):
    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'
    
    nome = models.CharField(max_length=250, null=False)
    local = models.CharField(max_length=250, null=False)
    data = models.DateField(null=False)
    time = models.TimeField(null=False)
    imagem = models.ImageField(upload_to='hobby', null=False)
    descricao = models.TextField(null=False)

    def __str__(self):
        return self.nome


