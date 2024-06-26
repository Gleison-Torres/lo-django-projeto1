from django.db import models
from stdimage import StdImageField
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Category(models.Model):
    objects = None
    name = models.CharField('Nome', max_length=30)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Base(models.Model):
    active = models.BooleanField('Publicado:', default=False)
    create = models.DateField('Criado', auto_now_add=True)
    modified = models.DateField('Modificado', auto_now=True)

    class Meta:
        abstract = True


class Recipe(Base):
    objects = None
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Criador')
    title = models.CharField('Titulo', max_length=50)
    description = models.TextField('Descrição', max_length=250)
    time_recipe = models.PositiveIntegerField('Preparo')
    image = StdImageField('Imagem', upload_to='imagens',
                          variations={'thumb': {'width': 1280, 'height': 720, 'crop': True}})
    order = models.PositiveIntegerField('Porções')
    step = models.TextField('Passo a passo', max_length=3000)
    recipe_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Categoria')
    slug = AutoSlugField(populate_from='title', unique=True)

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

    def __str__(self):
        return self.title
