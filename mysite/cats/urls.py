from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'cats'
urlpatterns = [
    # URL principal. /cats/
    path('', views.MainView.as_view(), name='all'),
    # URL para crear un automóvil
    path('main/create/', views.CatCreate.as_view(), name='cat_create'),
    # URL para actualizar y borrar, utiliza el pk
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    # URL para ir a mirar info de actuales fabricantes
    path('lookup/', views.BreedView.as_view(), name='breed_list'),
    # URL para crear un fabricante
    path('lookup/create/', views.BreedCreate.as_view(), name='breed_create'),
    # URL para actualizar y borrar un fabricante, utiliza pk
    path('lookup/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    path('lookup/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
]