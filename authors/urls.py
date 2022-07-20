from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.authors, name='register'),
    path('register/create/', views.authors_register_post, name='create')
]
