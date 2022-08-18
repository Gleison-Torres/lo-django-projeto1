from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.authors, name='register'),
    path('register/create/', views.authors_register_post, name='create'),
    path('login/', views.login_authenticate, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard_user, name='dashboard')
]
