from django.urls import path
from . import views

app_name = 'platos' 

urlpatterns = [
	path('',views.platos, name='platos'),
	path('<int:pk>/',views.detalles.as_view(), name='detalles_plato'),
	path('agregar/', views.agregar.as_view(), name='agregar_plato'),
	path('listar', views.listar.as_view(), name='listar_platos'),
	path('<int:pk>/modificar/', views.modificar.as_view(template_name='platos/platos_update.html'), name='modificar_plato'),
	path('<int:pk>/borrar/', views.eliminar.as_view(), name='eliminar_plato'),
	path('modificar',views.modificar2,name='editar_platos'),
	path('borrar',views.eliminar2,name='borrar_plato')
]
