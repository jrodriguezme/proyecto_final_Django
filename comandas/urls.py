from django.urls import path
from . import views
from . import apiViews

app_name = 'comandas' 

urlpatterns = [
	path('',views.comandas, name='comandas'),
	path('<int:pk>/',views.detalles, name='detalles_comandas'),
	path('agregar/', views.agregar.as_view(), name='agregar_comandas'),
	path('listar', views.listar.as_view(), name='listar_comandas'),
	path('<int:pk>/modificar/', views.modificar.as_view(template_name='comandas/formato_update.html'), name='modificar_comandas'),
	path('<int:pk>/borrar/', views.eliminar.as_view(), name='eliminar_comandas'),
	path('modificar',views.modificar2,name='editar_comandas'),
	path('borrar',views.eliminar2,name='borrar_comandas'),
	path('getFormato',apiViews.getFormato,name='formatos'),
	# path('prueba',views.myview,name='prueba')
]
