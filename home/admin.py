from django.contrib import admin
from . import models


@admin.register(models.Receita)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'recipe_category', 'active', 'create', 'modified', 'slug')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
