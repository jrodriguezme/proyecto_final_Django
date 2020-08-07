from django.urls import path
from . import views

app_name = 'comandas' 

urlpatterns = [
	path('',views.comanda.as_view(), name='comanda'),
	path('<int:pk>/',views.detalles.as_view(), name='detalles_comanda'),
	#path('agregar/', views.agregar.as_view(), name='agregar_comanda'),
	path('listar', views.listar.as_view(), name='listar_comandas'),
	path('<int:pk>/modificar/', views.modificar.as_view(template_name='comandas/formato_update.html'), name='modificar_comanda'),
	path('<int:pk>/borrar/', views.eliminar.as_view(), name='eliminar_comanda'),
	path('modificar',views.modificar2,name='editar_comanda'),
	path('borrar',views.eliminar2,name='borrar_comanda')
]
