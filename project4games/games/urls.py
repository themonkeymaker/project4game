from django.urls import path

from . import views

app_name = 'games'
urlpatterns = [
    path('', views.IndexView.as_view(), name='game-list'),
    path('<int:pk>/', views.DetailView.as_view(), name='game-detail'),
    path('create/', views.GameCreate.as_view(), name='game-create'),
    path('<int:pk>/update/', views.GameUpdate.as_view(), name='game-update'),
    path('<int:pk>/delete/', views.GameDelete.as_view(), name='game-delete'),
]