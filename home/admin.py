from django.contrib import admin
from . import models


@admin.register(models.Recipe)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'create', 'active', 'slug')
    list_display_links = ('title', 'create')
    search_fields = ('title', 'description', 'slug', 'step')
    list_filter = ('author', 'recipe_category', 'active')
    list_per_page = 10
    list_editable = ('active',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )

