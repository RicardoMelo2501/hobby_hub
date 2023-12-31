# Generated by Django 4.2.2 on 2023-10-25 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('local', models.CharField(max_length=250)),
                ('data', models.DateField()),
                ('time', models.TimeField()),
                ('imagem', models.ImageField(upload_to='hobby')),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name': 'Hobby',
                'verbose_name_plural': 'Hobbies',
            },
        ),
    ]
