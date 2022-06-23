from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/search/', views.search_recipe, name='search'),
    path('recipe/<int:pk>/', views.recipe, name='rec'),
    path('recipe/categories/<int:pk>/', views.category_recipe, name='cat')
]
