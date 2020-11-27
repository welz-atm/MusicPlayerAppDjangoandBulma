from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_track/', views.create_track, name='create_track'),
    path('delete_track/<int:pk>/', views.delete_track, name='delete_track'),
    path('play_track/<int:pk>/', views.play_track, name='play_track'),
    path('stop_track/<int:pk>/', views.stop_track, name='stop_track'),
    path('pause_track/<int:pk>/', views.pause_track, name='pause_track'),
    path('unpause_track/<int:pk>/', views.unpause_track, name='unpause_track'),
    path('like/<int:pk>/', views.is_like, name='is_like'),
    path('unlike/<int:pk>/', views.is_unlike, name='is_unlike'),

]
