from django.contrib import admin
from . import models


@admin.register(models.Receita)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'recipe_category', 'active', 'create', 'modified')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
