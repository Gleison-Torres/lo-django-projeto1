# Generated by Django 4.0.4 on 2022-06-27 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_recipe_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Receita', 'verbose_name_plural': 'Receitas'},
        ),
    ]
