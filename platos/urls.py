from django.urls import path
from . import views

app_name = 'platos' 

urlpatterns = [
	path('',views.platos, name='platos'),
	path('<int:pk>',views.detalles.as_view(), name='detalles_plato'),
	path('agregar', views.agregar.as_view(), name='agregar_plato'),
	path('listar', views.listar, name='listar_platos'),
	path('modificar', views.modificar, name='modificar_plato'),
	path('eliminar', views.eliminar, name='eliminar_plato'),
]
