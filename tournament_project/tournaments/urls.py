from django.urls import path
from . import views

urlpatterns = [
    path('', views.tournament_list, name='tournament_list'),
    path('tournament/<int:pk>/', views.tournament_detail, name='tournament_detail'),
    path('tournament/new/', views.tournament_create, name='tournament_create'),
    path('tournament/<int:pk>/edit/', views.tournament_update, name='tournament_update'),
    path('tournament/<int:pk>/delete/', views.tournament_delete, name='tournament_delete'),
]
