# Generated by Django 4.0.4 on 2022-06-16 01:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0009_alter_receita_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Receita',
            new_name='Recipe',
        ),
    ]
