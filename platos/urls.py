from django.urls import path
from . import views

urlpatterns = [
	path('',views.platos, name='platos'),
	path('agregar', views.agregar.as_view(), name='agregar plato'),
	path('listar', views.listar, name='listar platos'),
	path('modificar', views.modificar, name='modificar plato'),
	path('eliminar', views.eliminar, name='eliminar plato'),
]
