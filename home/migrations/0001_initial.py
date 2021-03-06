# Generated by Django 4.0.4 on 2022-06-09 19:31

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo:')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('description', models.TextField(max_length=250, verbose_name='Descrição')),
                ('time_recipe', models.PositiveIntegerField(verbose_name='Preparo')),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to='imagens', variations={'thumb': {'crop': True, 'height': 720, 'width': 1280}}, verbose_name='Imagem')),
                ('order', models.PositiveIntegerField(verbose_name='Porções')),
                ('step', models.TextField(max_length=3000, verbose_name='Passo a passo')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
