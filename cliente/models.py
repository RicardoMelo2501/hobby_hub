from django.db import models
from cliente.validators import validate_CPF_CNPJ

class Cliente(models.Model):
    SEXO_MASCULINO = 0
    SEXO_FEMININO = 1
    SEXO_DESCONHECIDO = 2

    LISTA_SEXO = (
        (SEXO_MASCULINO, 'Masculino'),
        (SEXO_FEMININO, 'Feminino'),
        (SEXO_DESCONHECIDO, 'Desconhecido / Não informado'),
    )

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    # Dados Pessoais
    nome = models.CharField(max_length=255, null=False, blank=False)
    sexo = models.SmallIntegerField('Gênero', choices=LISTA_SEXO, null=True, blank=True, default=None)
    cpf_cnpj = models.CharField('CPF', max_length=32, null=True, blank=True, default=None, db_index=True,validators=[validate_CPF_CNPJ])
    rg_numero = models.CharField(u'Nº RG', max_length=32, null=True, blank=True, default=None)
    data_nascimento = models.DateField('Data de nascimento', null=True, blank=True, default=None)
    email = models.CharField(max_length=255)
    contato = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    estado_civil = models.CharField(max_length=255)

    # Endereço
    cep = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    numero_residencia = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
