from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'autos'
urlpatterns = [
    # URL principal. /autos/
    path('', views.MainView.as_view(), name='all'),
    # URL para crear un automóvil
    path('main/create/', views.AutoCreate.as_view(), name='auto_create'),
    # URL para actualizar y borrar, utiliza el pk
    path('main/<int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),
    path('main/<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),
    # URL para ir a mirar info de actuales fabricantes
    path('lookup/', views.MakeView.as_view(), name='make_list'),
    # URL para crear un fabricante
    path('lookup/create/', views.MakeCreate.as_view(), name='make_create'),
    # URL para actualizar y borrar un fabricante, utiliza pk
    path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
    path('lookup/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),
]
