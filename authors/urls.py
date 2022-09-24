from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.authors, name='register'),
    path('register/create/', views.authors_register_post, name='create'),
    path('login/', views.login_authenticate, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard_user, name='dashboard'),
    path('dashboard/approved/', views.dashboard_approved, name='approved'),
    path('dashboard/pending/', views.dashboard_pending, name='pending'),
    path('dashboard/category/<int:pk>/', views.dashboard_user_category, name='category'),
    path('recipe/', views.sending_recipe, name='recipe'),
    path('recipe/send/', views.sending_recipe_post, name='recipe_post'),
    path('dashboard/recipe/<int:pk>/edit/', views.dashboard_edit_recipe, name='edit'),
    path('dashboard/recipe/<int:pk>/delete/', views.dashboard_delete_recipe, name='delete')
]
