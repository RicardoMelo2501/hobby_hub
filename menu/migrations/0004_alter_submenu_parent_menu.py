# Generated by Django 4.2.2 on 2023-06-16 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_submenu_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu',
            name='parent_menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='menu.menu'),
        ),
    ]
