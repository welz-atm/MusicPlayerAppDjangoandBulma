from django.urls import path
from .import views

urlpatterns = [
    path('register_user', views.register, name='register'),
    path('edit_user/<int:pk>/', views.edit_user, name='edit_user'),
    path('login/', views.login_user, name='login'),
    path('change_password/', views.change_password, name='change_password'),
    path('logout/', views.logout, name='logout'),
]
