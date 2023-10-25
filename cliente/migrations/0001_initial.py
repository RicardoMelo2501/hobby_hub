# Generated by Django 4.2.2 on 2023-08-29 02:33

import cliente.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sexo', models.SmallIntegerField(blank=True, choices=[(0, 'Masculino'), (1, 'Feminino'), (2, 'Desconhecido / Não informado')], default=None, null=True, verbose_name='Gênero')),
                ('cpf_cnpj', models.CharField(blank=True, db_index=True, default=None, max_length=32, null=True, validators=[cliente.validators.validate_CPF_CNPJ], verbose_name='CPF')),
                ('rg_numero', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='Nº RG')),
                ('data_nascimento', models.DateField(blank=True, default=None, null=True, verbose_name='Data de nascimento')),
                ('email', models.CharField(max_length=255)),
                ('contato', models.CharField(max_length=255)),
                ('genero', models.CharField(max_length=255)),
                ('estado_civil', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('municipio', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('logradouro', models.CharField(max_length=255)),
                ('numero_residencia', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]