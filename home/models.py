from django.db import models
from stdimage import StdImageField


class Base(models.Model):
    active = models.BooleanField('Ativo:', default=True)
    create = models.DateField('Criado', auto_now_add=True)
    modified = models.DateField('Modificado', auto_now=True)

    class Meta:
        abstract = True


class Receita(Base):
    TYPE_RECIPE_CHOICES = (
        ('Café da manhã', 'Café da manhã'),
        ('Almoço', 'Almoço'),
        ('Massa', 'Massa'),
        ('Doce', 'Doce'),
        ('Sobremesa', 'Sobremesa'),
        ('Lanche', 'Lanche')
    )

    title = models.CharField('Titulo', max_length=50)
    category = models.CharField('Categoria', choices=TYPE_RECIPE_CHOICES, max_length=14)
    description = models.TextField('Descrição', max_length=250)
    time_recipe = models.PositiveIntegerField('Preparo')
    image = StdImageField('Imagem', upload_to='imagens', variations={'thumb': {'width': 1280, 'height': 720, 'crop': True}})
    order = models.PositiveIntegerField('Porções')
    step = models.TextField('Passo a passo', max_length=3000)

    def __str__(self):
        return self.title


