from django.contrib import admin
from . import models


@admin.register(models.Receita)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'active', 'create', 'modified')


