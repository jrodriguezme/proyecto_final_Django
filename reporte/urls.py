from django.urls import path
from . import views

app_name = 'reporte' 

urlpatterns = [
	path('',views.reserva, name='reserva'),
	path('<int:pk>/',views.detalles.as_view(), name='detalles_reserva'),
	path('agregar/', views.agregar.as_view(), name='agregar_reserva'),
	path('listar', views.listar.as_view(), name='listar_reserva'),
	path('<int:pk>/modificar/', views.modificar.as_view(template_name='reporte/reserva_update.html'), name='modificar_reserva'),
	path('<int:pk>/borrar/', views.eliminar.as_view(), name='eliminar_reserva'),
	path('modificar',views.modificar2,name='editar_reserva'),
	path('borrar',views.eliminar2,name='borrar_reserva')
]
